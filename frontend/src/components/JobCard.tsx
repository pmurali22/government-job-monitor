interface JobCardProps {
  title: string
  company: string
  location: string
}

function JobCard({ title, company, location }: JobCardProps) {
  return (
    <div className="job-card">
      <h2>{title}</h2>
      <p>{company}</p>
      <p>{location}</p>
    </div>
  )
}

export default JobCard
