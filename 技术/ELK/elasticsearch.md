## 数据库操作

```bash
curl -H "Content-Type: application/json" localhost:9200/test_index_1221/test_type/5 -d '{"user_name":"xiaoming"}'
>>>{"_index":"test_index_1221","_type":"test_type","_id":"5","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1}
```

## 查询

使用 [Match 查询](https://www.elastic.co/guide/en/elasticsearch/reference/5.5/query-dsl-match-query.html)，指定的匹配条件是`desc`字段里面包含"软件"这个词

```bash
$ curl 'localhost:9200/accounts/person/_search'  -d '
{
  "query" : { "match" : { "desc" : "软件" }}
}'
```

使用python脚本

```python
url = 'http://47.107.234.148/accounts/person/_search'
h = {
    "Content-Type": "application/json"
}
d = {
    "query": {'match': {'user': 'zhang wang'}},  # zhang or wang
    "size": 100,  # 默认是10
    "from": 1,    # 指定位移
}
print json.dumps(d)
r = requests.post(url, data=json.dumps(d), headers=h)
print r.json()
```

## python开发

```python
pip install elasticsearch	
```

