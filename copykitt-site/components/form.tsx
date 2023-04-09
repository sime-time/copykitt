interface FormProps {
  prompt: string;
  setPrompt: any;
  onSubmit: any;
}


const Form: React.FC<FormProps> = (props) => {

const characterLimit = 32;
const isPromptValid = props.prompt.length <= 32;

  return (
    <>      
      <p>Tell me what your brand is about and I will generate copy and keywords for you.</p>
      <input 
        type="text" 
        placeholder="coffee" 
        value={props.prompt}
        onChange={(e) => props.setPrompt(e.currentTarget.value)}
      ></input>
      <div>{props.prompt.length}/{characterLimit}</div>
      <button onClick={props.onSubmit}>Submit</button>
    </>
  );
};

export default Form; 