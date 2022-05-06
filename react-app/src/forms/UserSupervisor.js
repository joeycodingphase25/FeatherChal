import React, { useEffect, useState } from 'react'

export default function UserSupervisor(props) {
    // create flash message in app.js to pass through props
    // const { flashMessage } = props;

    // handles dropdown
    const [supervisors, setSupervisors] = useState([]) // grab the list of eras from era
    const [chosen, setChosen] = useState(null) // dynamic drop down menu force a selection of a supervisor

    useEffect( () => {
        fetch("http://127.0.0.1:5000/api/supervisors")
            .then(res => res.json())
            .then(supervisors => setSupervisors(supervisors))
    }, []) 


    const handleSubmit = (e) => {
        e.preventDefault();

        let myHeaders = new Headers();
        myHeaders.append('Content-Type', 'application/json');
        // creating variable to pull from form 
        let firstName = e.target.firstName.value;
        let lastName = e.target.lastName.value;
        let supervisor = chosen; // Implement this later
        let email = e.target.email.value;
        let phoneNumber = e.target.phoneNumber.value;
        
        // consolidate and fetch data from flask backend
        let data = JSON.stringify({firstName, lastName, email, phoneNumber, supervisor})
        
        fetch("http://127.0.0.1:5000/api/submit", {
            method: "POST",
            headers: myHeaders,
            body: data
        }).then(res => res.json())
            .then(data => {
                if (data.error){
                    console.error(data.error)
                }else {
                    props.flashMessage(`Thank you ${firstName}, Notification Success!`, 'success')
                }
            })
    }
    return (
        <>
        <form onSubmit={handleSubmit}>
            <h3 className='text-center mt-3'>Create New User</h3>
            <h5>Enter Information Below</h5>
            <div className='form-group'>

                <label htmlFor='firstName'>First Name</label>
                <input type='text' name='firstName' className='form-control' placeholder='Enter First Name' />

                <label htmlFor='lastName'>Last Name</label>
                <input type='text' name='lastName' className='form-control' placeholder='Enter Last Name'/>
                
                <label htmlFor='email'>Email</label>
                <input type='text' name='email' className='form-control' placeholder='Enter Your Email Here' />
                
                <label htmlFor='phoneNumber'>Phone Number</label>
                <input type='text' name='phoneNumber' className='form-control' placeholder='Enter Your Phone Number Here (XXX) XXX-XXXX' />
                
                {/* Select Drop Down here for supervisors */}
                {/* This needs troubleshooting and testing */}
                <select defaultValue='default' className='w-100 mt-3'onChange={(e)=>setChosen(e.target.value)}>
                {supervisors.map((supervisor, idx) => <option key={idx} value={supervisor.jurisdiction}>{`<${supervisor.jurisdiction}>-<${supervisor.firstName}>, <${supervisor.lastName}>`}</option>)} 
                    <option value='default' disabled>Choose supervisor..</option>
                </select>



                <input type='submit' className='btn btn-outline-dark w-100 p-3 mt-3' value='Create User' />
            </div>
        </form>
        </>
        )
}
