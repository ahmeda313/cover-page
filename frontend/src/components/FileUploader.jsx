import { useState } from "react"

export default function FileUploader({setResult}){
    const [selectedFile, setSelectedFile] = useState(null)
    const [inputErr, setInputErr] = useState(null)

    async function submitFile(){
        if(selectedFile === null){
            console.log("please select valid file")
            setInputErr(true)
            return
        }
        setResult("loading")

        const res = await fetch("http://127.0.0.1:5000/upload",{
            method:"POST",
            body:selectedFile
        })

        const result = await res.json()

        console.log(result)
        
        setResult(result)

    }

    function selectingFunction(e){
        const formData = new FormData();
        formData.append('file', e.target.files[0]); 
        setInputErr(false)
        setSelectedFile(formData)
    }

    return(
        <>
    <div className="flex items-center justify-center w-1/2 mx-auto">
        <label htmlFor="dropzone-file" className="flex flex-col items-center justify-center w-full h-52 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
            <div className="flex flex-col items-center justify-center pt-5 pb-6">
                <svg className="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                    <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                </svg>
                <p className="mb-2 text-sm text-gray-500 dark:text-gray-400"><span className="font-semibold">Click to upload</span> or drag and drop</p>
                <p className="text-xs text-gray-500 dark:text-gray-400">*.docx files only</p>
            </div>
            <input id="dropzone-file" type="file" className="hidden" accept=".docx" onChange={selectingFunction} />
        </label>
    </div> 
    {inputErr !==null && <p className={`text-center mt-3 ${inputErr ? "text-red-800":"text-green-600"}`}>{inputErr ? "No file found":selectedFile.get('file').name}</p>}
    <div className="flex mt-4">
        <button className="mx-auto text-xl text-white font-bold bg-green-700 px-3 py-2 rounded-lg hover:bg-green-600" onClick={submitFile}>Generate</button>
    </div>
    </>


    )
}