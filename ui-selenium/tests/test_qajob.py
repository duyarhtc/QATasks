from pages.qajob_page import QAJobsPage


def test_qa_jobs_filter(driver):
    qa = QAJobsPage(driver)

    qa.load()
    qa.click_see_all_jobs()

    # Filter → Istanbul
    qa.filter_by_location()

    # Filter → Quality Assurance
    qa.filter_by_department()

    assert qa.verify_job_list_exists(), "ERROR: No job list found after filter!"

    assert qa.verify_job_list_visible(), "ERROR: Job cards are not visible on the UI!"
    
    assert qa.verify_job_details(), "ERROR: Some job cards have incorrect info!"
   
    qa.click_last_job_view_role()

    assert qa.test_view_role_redirects_to_lever(), "ERROR: Lever tab was not verified"
