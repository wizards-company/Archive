'use client';
import React from 'react';

function MyPage() {
  return (
    <main>
      <h2>User Registration</h2>
      <form>
        <label>Name:</label><br />
        <input type="text"></input><br />
        <label>Email:</label><br />
        <input type="email"></input><br />
        <label>Password:</label><br />
        <input type="password"></input><br /><br />
        <input type="submit" ></input>
      </form>
    </main>
  );
}

export default MyPage;