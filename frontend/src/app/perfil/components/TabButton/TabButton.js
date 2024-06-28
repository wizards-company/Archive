import style from "./TabButton.module.css"

export default function TabButton({text, isSelected, handleSelect}) {
  return (
    <button onClick={handleSelect} className={`${style.button} ${isSelected ? style.btnSelected : style.btnUnselected}`}>{text}</button>
  )
}