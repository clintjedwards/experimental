FROM golang:1.13 AS build-environment

ADD . /files
WORKDIR /files

ENV GOOS=linux GOARCH=amd64 CGO_ENABLED=0

RUN make build SEMVER=1.0.0 BUILD_PATH=/build/experimental build

FROM gcr.io/distroless/static
WORKDIR /app
COPY --from=build-environment /build/experimental /app/experimental
ENTRYPOINT [ "./experimental" ]
