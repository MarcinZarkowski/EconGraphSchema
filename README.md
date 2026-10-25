# EconGraphSchema

# Generate Go code
export PATH="$PATH:$HOME/go/bin"                     

protoc \
  --proto_path=proto/v1 \
  --go_out=clients/go/v1 \
  --go_opt=paths=source_relative \
  proto/v1/*.proto


# Generate Python code 

protoc \
  --proto_path=proto/v1 \
  --python_out=clients/python/v1 \
  --pyi_out=clients/python/v1 \
  proto/v1/*.proto
