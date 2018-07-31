var http = require('http').createServer(LoadPage);
var fs = require('fs');
var spawn = require('child_process').spawn;
var py = spawn('python', ['LoadCapturedImageDetails.py']);
var html = '<!DOCTYPE html><html><body><h1>Camera Trap</h1><table style="width:100%" border="1">';
html += '<tr><th>Index</th><th>Capture Time</th><th>Location</th></tr>';
console.log('Reloading using python...');
py.stdout.on('data', function(data)
{
	console.log('Got data');
	var strData = data.toString();
	console.log(strData);
	var rows = strData.split("(");
	for(i=0;i<rows.length;i++)
	{
		var cells = rows[i].split(",");
		html += '<tr>';
	
		for(j=0;j<cells.length;j++)
		{
			html += '<td>' + cells[j] + '</td>';
		}
	
		html += '</tr>';
	}
});

py.stdout.on('end', function()
{
	html += '</table></body></html>';
	console.log(html);
	
});

py.stdin.end();

var imageDir = '/home/pi/CameraCaptures/';
console.log('Looking in ' + imageDir);
http.listen(8080);
console.log('Ready to load images');

function LoadPage(req, res)
{		
	res.writeHead(200, {'Content-Type' : 'text/html'}); 	
	console.log('Returning ' + html);
	return res.end(html, 'utf-8');		
}



