import fs from 'fs';
import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: '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',
  baseURL: 'https://integrate.api.nvidia.com/v1',
});

async function main() {
  // Lee el contenido del archivo
  const filePath = './PROGRAM 15-4/PROG15-4.COB'; // ruta del tu archivo
  const fileContent = fs.readFileSync(filePath, 'utf-8');

  // Envía el contenido del archivo como promt
  const completion = await openai.chat.completions.create({
    model: "ibm/granite-34b-code-instruct",
    messages: [
      {
        role: "user",
        content: "Hola, podrias explicarme que hace este programa?:\n\n" + fileContent,
      },
    ],
    temperature: 0.5,
    top_p: 1,
    max_tokens: 1024,
    stream: true,
  });

  let response = '';
  for await (const chunk of completion) {
    response += chunk.choices[0]?.delta?.content || '';
  }

  console.log('Full response:', response);
}

main();
