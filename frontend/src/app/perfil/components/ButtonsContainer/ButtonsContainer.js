"use client"
import TabButton from "../TabButton/TabButton"
import style from "./buttonsContainer.module.css"
import { useState } from "react"

export default function ButtonsContainer({ setSelectBtn, selectBtn }) {
  // const [selectBtn, setSelectBtn] = useState(0)

  return (
    <div className={style.container}>
      <TabButton
        isSelected={selectBtn == 0}
        handleSelect={() => setSelectBtn(0)}
        text="Artigos"
      />
      <TabButton
        isSelected={selectBtn == 1}
        handleSelect={() => setSelectBtn(1)}
        text="Doações"
      />
      <TabButton
        isSelected={selectBtn == 2}
        handleSelect={() => setSelectBtn(2)}
        text="Salvos"
      />
    </div>
  )
}
