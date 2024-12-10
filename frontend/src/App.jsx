import { useState } from "react"
import FileUploader from "./components/FileUploader"
import Results from "./components/Results"


function App() {
  const [result, setResult] = useState(null)

  return (
    <>
    <FileUploader setResult={setResult}/>
    {result && <Results result={result}/>}
    </>
  )
}

export default App
