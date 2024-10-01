import React from 'react';

// Define the interface for the props
interface TODO {
  title: string;
  description: string;
  status: boolean;
  email?: string; // Optional property
}

// Define the Render component with props typed as TODO
function Render(props: TODO) {
  return (
    <div>
      <h1>{props.title}</h1>
      <p>{props.description}</p>
      <p>Status: {props.status ? 'Completed' : 'Not Completed'}</p>
      {props.email && <p>Email: {props.email}</p>}
    </div>
  );
}

// Define the App component
function App() {
  return (
    <Render
      title="Task Title"
      description="Task Description"
      status={true}
    />
  );
}

export default App;
