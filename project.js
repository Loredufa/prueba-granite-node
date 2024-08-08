import fs from 'fs';
import OpenAI from 'openai';
import path from 'path';

const openai = new OpenAI({
  apiKey: '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',
  baseURL: 'https://integrate.api.nvidia.com/v1',
});

// Función para verificar si una extensión es de texto
function isTextFile(filePath) {
  const textExtensions = ['.cbl', '.jcl', '.md', '.txt', '.json', '.js', '.java', '.py', '.html', '.css', '.cob', '.dat'];
  const ext = path.extname(filePath).toLowerCase();
  return textExtensions.includes(ext);
}

async function readDirectory(directoryPath) {
  let filePaths = [];
  console.log("Leyendo el directorio...");
  const files = fs.readdirSync(directoryPath);

  for (const file of files) {
    const filePath = path.join(directoryPath, file);
    console.log(`Encontrado: ${filePath}`);
    const stats = fs.statSync(filePath);

    if (stats.isFile() && isTextFile(filePath)) {
      filePaths.push(filePath);
    } else if (stats.isDirectory() && !filePath.includes('.git')) {
      const nestedPaths = await readDirectory(filePath);
      filePaths = filePaths.concat(nestedPaths);
    }
  }
  console.log('FILEPATHS', filePaths)
  return filePaths;
}

async function main() {
  const projectPath = './PROGRAM 15-4'; // Ruta a tu carpeta de proyecto
  console.log("Comenzando la función...");

  try {
    const filePaths = await readDirectory(projectPath);
    console.log("Finaliza lectura de archivos...");
    console.log('Archivos encontrados:', filePaths);
    
    let consolidatedResponse = '';

    for (const filePath of filePaths) {
      console.log(`Leyendo archivo: ${filePath}`);
      const fileContent = fs.readFileSync(filePath, 'utf-8');
      
      // Divide el contenido en partes si es demasiado largo para una sola solicitud
      const chunkSize = 5000; // Ajusta según el límite de tokens
      const chunks = fileContent.match(new RegExp(`.{1,${chunkSize}}`, 'gs')) || [];

      for (const chunk of chunks) {
        try {
          const completion = await openai.chat.completions.create({
            model: "ibm/granite-34b-code-instruct",
            messages: [
              {
                role: "user",
                content: "Hola, Actua como experto en COBOL y JAVASCRIPT y por favor migra la aplicacion de COBOL a lenguaje JavaScript, proporcionarme el codigo completo\n\n" + chunk,
              },
            ],
            temperature: 0.5,
            top_p: 1,
            max_tokens: 1024,
            stream: false, // Cambiado a false para una respuesta síncrona
          });

          // Consolida la respuesta del modelo
          consolidatedResponse += completion.choices[0].message.content || '';
        } catch (error) {
          console.error("Error llamando al modelo:", error);
        }
      }
    }

    console.log('Respuesta consolidada del modelo:', consolidatedResponse);
  } catch (error) {
    console.error("Error en la función principal:", error);
  }
}

main();




