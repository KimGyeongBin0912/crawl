from fastapi import FastAPI, Query
from crawler.dbpia import crawl_dbpia
from crawler.riss import crawl_riss
from crawler.kci import crawl_kci

app = FastAPI()

@app.get("/crawl/dbpia")
def dbpia(query: str = Query(...)):
    return {"results": crawl_dbpia(query)}

@app.get("/crawl/riss")
def riss(query: str = Query(...)):
    return {"results": crawl_riss(query)}

@app.get("/crawl/kci")
def kci(query: str = Query(...)):
    return {"results": crawl_kci(query)}
