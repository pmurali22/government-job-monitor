import JobCard from '../components/JobCard'

function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <p>View the latest matched job postings.</p>
      <JobCard title="Sample Job" company="Official Agency" location="Remote" />
    </div>
  )
}

export default Dashboard
