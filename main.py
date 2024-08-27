from fastapi import FastAPI, Request
import uvicorn
from random import randint
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import time 

counter_prometheus = Counter('my_requests_total', 'HTTP Failures', ['method', 'endpoint', 'status'])

trace.set_tracer_provider(TracerProvider())

 # Exportar para sidecar jaeger-agent
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost", 
    agent_port=6831,              
)

span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

tracer = trace.get_tracer("diceroller.tracer")

app = FastAPI()

FastAPIInstrumentor.instrument_app(app)

@app.get("/")
async def root():
    counter_prometheus.labels(method='get', endpoint='/', status=200).inc()
    return {"msg": "Hello World!!"}

@app.get("/pr")
async def pr():
    counter_prometheus.labels(method='get', endpoint='/', status=200).inc()
    return {"msg":"Olá! Você está na minha aplicação de estudos Git e API"}

@app.get("/actions")
async def actions():
    return {"msg":"Testando o Actions"}

@app.get("/metrics")
async def metrics():
    return generate_latest()

@app.get("/health")
async def health_check():
    if True:  # apenas para fins de estudo health docker
        return {"status": "ok"}
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")

"""
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
    """