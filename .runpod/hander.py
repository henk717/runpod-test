import runpod
def handler(event):
    result = "Hi! Want to use KoboldCpp on serverless? You can! But it must be a load balanced instance, this is the only thing we support."
    
    # Return the result
    return result

runpod.serverless.start({"handler": handler})
