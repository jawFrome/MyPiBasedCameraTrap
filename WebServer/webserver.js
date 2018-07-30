var http = require('http').createServer(handler);
var fs = require('fs');

http.listen(8080);

function handler(req, res)
{
	fs.readFile('/home/pi/Documents/CameraTrap/WebServer/index.html',
	function(err, data)
	{
		if(err)
		{
			res.writeHead(404, {'Content-Type' : 'text/html'});
			return res.end(err.message); // "404 Not Found");
		}
		
		res.writeHead(202, {'Content-Type' : 'text/html'}); 
		res.write(data);
		return res.end();
	});
}