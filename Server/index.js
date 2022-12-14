
const os = require('os')
const http = require('http')
const port = 3000
const hostname=os.hostname()
const server = http.createServer((req, res) => {
    res.statusCode = 200
    res.setHeader('Content-Type', 'text/plain')
    res.end(BuildData())
    
    
})
server.listen(port, () => {
    console.log(`服务器运行在 http://${hostname}:${port}/`)
})
function BuildData() {
    var JsonObject = {
        "hostname": os.hostname(),
        "cpu_model": os.cpus()[0]["model"],
        "freemem": (os.freemem() / 1048576).toFixed(1),
        "totalmem": (os.totalmem() / 1048576).toFixed(1),
        "cpu_model":os.cpus()[0]["model"]
    };
    var JsonString = JSON.stringify(JsonObject); //将json对象转换为字符串
    //console.log(JsonString)
    return (JsonString);
}
