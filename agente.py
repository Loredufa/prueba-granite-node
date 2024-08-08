import os

from openai import OpenAI

# Available OpenAI models
ORCHESTRATOR_MODEL = "ibm/granite-34b-code-instruct"

#client = OpenAI(
#  base_url = "https://integrate.api.nvidia.com/v1",
#  api_key = ""
#)

def agente(tarea):
    # Dividir la tarea en fragmentos pequeños si es necesario
    max_chunk_size = 1024  # Tamaño máximo de cada fragmento
    task_chunks = [tarea[i:i + max_chunk_size] for i in range(0, len(tarea), max_chunk_size)]
    
    responses = []
    for chunk in task_chunks:
        prompt = f"""
        Actúa como developer senior y responde solo con código, sin ninguna explicación. 
        {chunk}
        """
        try:
            completion = client.chat.completions.create(
                model=ORCHESTRATOR_MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=2048,  # Asegúrate de que no exceda el límite permitido
                stream=False
            )
            responses.append(completion.choices[0].message.content.strip())
        except Exception as e:
            print(f"Error al ejecutar el agente: {e}")
            return None
    
    # Unir todas las respuestas en una sola
    result = "\n".join(responses)
    print(f'Resultado del agente: {result}')
    return result
