SEMVER = v1.0.0
GO_LDFLAGS = '-X "main.version=$(SEMVER)"'
BUILD_PATH = /tmp/test

## build: run tests and compile full app in production mode
build:
	go mod tidy
	go build -ldflags $(GO_LDFLAGS) -o $(BUILD_PATH)

build_logs:
	go mod tidy
	go build -ldflags $(GO_LDFLAGS) -o $(BUILD_PATH) logs.go

build_fail:
	go mod tidy
	go build -ldflags $(GO_LDFLAGS) -o $(BUILD_PATH) fail.go

build_wait:
	go mod tidy
	go build -ldflags $(GO_LDFLAGS) -o $(BUILD_PATH) wait.go

# Test change 1
# Test change 2
