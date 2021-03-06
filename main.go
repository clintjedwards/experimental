package main

import (
	"bytes"
	"fmt"
	"html/template"
	"log"
	"net/http"
	"os"
	"runtime"
)

var version = "test"

var testpage = `
<html>
  <body>
    <h1>Hello World!</h1>
    <h2>Version: {{.Version}}</h2>
    <h2>OS: {{.OS}}</h2>
	<h2>Hostname: {{.Hostname}}</h2>
	<h2>Test Environment Variable: {{.TestEnv}}</h2>
  </body>
</html>
`

func main() {
	http.HandleFunc("/", HelloServer)
	log.Println("started webserver")
	http.ListenAndServe("0.0.0.0:8080", nil)
}

func parseTemplate(content string, data interface{}) (output []byte, err error) {
	var buf bytes.Buffer

	template, err := template.New("").Parse(content)
	if err != nil {
		return nil, err
	}
	err = template.Execute(&buf, data)
	if err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}

// HelloServer returns a test webserver
func HelloServer(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/html")

	hostname, _ := os.Hostname()

	testEnv := os.Getenv("TEST_ENV")

	template, err := parseTemplate(testpage, map[string]string{
		"Version":  version,
		"OS":       fmt.Sprintf("%s/%s", runtime.GOOS, runtime.GOARCH),
		"Hostname": hostname,
		"TestEnv":  testEnv,
	})
	if err != nil {
		log.Println(err)
	}

	fmt.Fprintf(w, string(template))
}
