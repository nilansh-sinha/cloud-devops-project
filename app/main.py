import time
from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Histogram

app = FastAPI(title="Secure Cloud-Native App")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Prometheus Metrics
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "HTTP request latency")

@app.middleware("http")
async def add_metrics(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    # Skip metrics for static files to keep noise down
    if not request.url.path.startswith("/static"):
        duration = time.time() - start_time
        REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
        REQUEST_LATENCY.observe(duration)
    
    return response

@app.get("/")
def read_root():
    return FileResponse('app/static/index.html')

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/metrics")
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
