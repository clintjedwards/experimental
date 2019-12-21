GO_LDFLAGS = '-X "github.com/clintjedwards/test/main.version=$(VERSION)"'
VERSION = v1.0.1
BUILD_PATH = /tmp/test

## build: run tests and compile full app in production mode
build:
	go mod tidy
	go build -race -ldflags $(GO_LDFLAGS) -o $(BUILD_PATH)
