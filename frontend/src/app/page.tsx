'use client'

import { useRouter } from 'next/navigation'

export default function Page() {
  const router = useRouter()

  return (
    <main>
      <h2>Index</h2>

      <button type="button" onClick={() => router.push('/register')}>
        Cadastrar novo usuario
      </button>
    </main>
  )
}