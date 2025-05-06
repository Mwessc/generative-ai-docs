VLLM_DOCKER_URI = "us-docker.pkg.dev/deeplearning-platform-release/vertex-model-garden/vllm-inference.cu121.0-6.ubuntu2204.py310"

model_name = "deepseek-ai-r1-1-5b"
model_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"

machine_type = "g2-standard-12"
accelerator_type = "NVIDIA_L4"
accelerator_count = 1

service_account = ""

endpoint = aiplatform.Endpoint.create(display_name=f"{model_name}-endpoint")

dtype = "bfloat16"
vllm_args = [
    "python",
    "-m",
    "vllm.entrypoints.api_server",
    "--host=0.0.0.0",
    "--port=7080",
    f"--model={model_id}",
    f"--tensor-parallel-size={accelerator_count}",
    "--swap-space=16",
    f"--dtype={dtype}",
    "--gpu-memory-utilization=0.95",
    "--max-model-len=32768",
    "--enforce-eager",
    "--disable-log-stats",
]
model = aiplatform.Model.upload(
    display_name=model_name,
    serving_container_image_uri=VLLM_DOCKER_URI,
    serving_container_args=vllm_args,
    serving_container_ports=[7080],
    serving_container_predict_route="/generate",
    serving_container_health_route="/ping",
)

model.deploy(
    endpoint=endpoint,
    machine_type=machine_type,
    accelerator_type=accelerator_type,
    accelerator_count=accelerator_count,
    service_account=service_account,
    # Set `disable_container_logging = True, fast_tryout_enabled=True,`
    # to deploy models with faster deploy option.
)

instances = [
    {
        "prompt": "What is 1+1? Please solve this math problem as a single number and put your final answer within \boxed{}.",
        "max_tokens": 200,
        "temperature": 0.6,
        "top_p": 1.0,
        "top_k": -1,
    }
]

response = endpoint.predict(instances=instances)
print(response.predictions[0])
# Set 'use_dedicated_endpoint=True' if using Fast Deploy Option)
