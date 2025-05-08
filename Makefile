IMAGE_NAME=batch-processing-repo
TAG=latest
REGION=ap-northeast-1
ECR_REPO_NAME=batch-processing-repo

build:
	docker build -f docker/Dockerfile -t $(IMAGE_NAME):$(TAG) .

run:
	docker run --rm -v $(PWD)/app/src:/batch $(IMAGE_NAME):$(TAG)

push:
	@ACCOUNT_ID=$$(aws sts get-caller-identity --query Account --output text); \
	docker tag $(ECR_REPO_NAME):latest $$ACCOUNT_ID.dkr.ecr.$(REGION).amazonaws.com/$(ECR_REPO_NAME):latest; \
	aws ecr get-login-password --region $(REGION) | docker login --username AWS --password-stdin $$ACCOUNT_ID.dkr.ecr.$(REGION).amazonaws.com; \
	docker push $$ACCOUNT_ID.dkr.ecr.$(REGION).amazonaws.com/$(ECR_REPO_NAME):latest

buildx:
	@ACCOUNT_ID=$$(aws sts get-caller-identity --query Account --output text); \
	aws ecr get-login-password --region $(REGION) | docker login --username AWS --password-stdin $$ACCOUNT_ID.dkr.ecr.$(REGION).amazonaws.com; \
	docker buildx build -f docker/Dockerfile --platform linux/amd64,linux/arm64 -t $$ACCOUNT_ID.dkr.ecr.$(REGION).amazonaws.com/$(ECR_REPO_NAME):latest . --push

# イメージを削除
clean:
	docker rmi $(IMAGE_NAME):$(TAG) || true

