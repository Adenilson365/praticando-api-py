from fastapi import FastAPI, Request, HTTPException
import uvicorn
import random
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time 

counter_prometheus = Counter('endpoint_request', 'Tesste de contagem de requests', ['method', 'endpoint', 'status'])

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
    counter_prometheus.labels(method='get', endpoint='/', status='200').inc()
    return {"msg": "Hello World!!"}

@app.get("/teste")
async def root():
    counter_prometheus.labels(method='get', endpoint='/', status='200').inc()
    return {"msg": "Teste Webhook"}

@app.get("/pr")
async def pr():
    # Gerar um número aleatório entre 0 e 1
    if random.random() < 0.3:  # +-30% de chance de retornar um erro 400
        counter_prometheus.labels(method='get', endpoint='/pr', status='400').inc()
        raise HTTPException(status_code=400, detail="Bad Request")
    
    # Contador para as requisições bem-sucedidas
    counter_prometheus.labels(method='get', endpoint='/pr', status='200').inc()
    return {"msg": "Olá! Você está na minha aplicação de estudos Git e API"}

@app.get("/actions")
async def actions():
    counter_prometheus.labels(method='get', endpoint='/actions', status='200').inc()
    return {"msg":"Testando o Actions"}

@app.get("/metrics")
async def metrics():
    counter_prometheus.labels(method='get', endpoint='/metrics', status='200').inc()
    from starlette.responses import Response
    content = generate_latest()
    return Response(content=content, media_type=CONTENT_TYPE_LATEST)

@app.get("/health")
async def health_check():
    counter_prometheus.labels(method='get', endpoint='/health', status='200').inc()
    return {"status": "ok"}


