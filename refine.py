import os

from openai import OpenAI

# Available OpenAI models
ORCHESTRATOR_MODEL = "ibm/granite-34b-code-instruct"

#client = OpenAI(
#  base_url="https://integrate.api.nvidia.com/v1",
#  api_key=""
#)

def refine(codigo_agente):
    # Dividir el código en fragmentos más pequeños
    max_chunk_size = 2048  # Tamaño máximo de cada fragmento en tokens
    task_chunks = [codigo_agente[i:i + max_chunk_size] for i in range(0, len(codigo_agente), max_chunk_size)]
    responses = []
    
    for chunk in task_chunks:
        prompt = f"""
        Actúa como un especialista en revisión de código. 
        Revisa el siguiente código generado por el agente senior y asegúrate de que sigue las mejores prácticas de codificación.
        Responde solo con código, sin ninguna explicación. 
        {chunk}
        """
        
        try:
            completion = client.chat.completions.create(
                model=ORCHESTRATOR_MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=2048,  # Ajusta esto a la longitud permitida
                stream=False
            )
            
            # Obtener y almacenar la respuesta
            responses.append(completion.choices[0].message.content.strip())
        
        except Exception as e:
            print(f"Error al ejecutar el refine: {str(e)}")
            return None
    
    # Unir todas las respuestas en una sola
    result = "\n".join(responses)
    print(f'Resultado del refine: {result}')
    return result

