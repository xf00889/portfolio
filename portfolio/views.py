from django.shortcuts import render

# Dictionary to store portfolio content
portfolio_content = {
    'about': {
        'name': 'Your Name',
        'title': 'Web Developer',
        'bio': 'Passionate web developer with expertise in creating modern web applications.',
        'skills': ['Python', 'Django', 'JavaScript', 'HTML/CSS', 'React', 'SQL']
    },
    'projects': [
        {
            'title': 'Project 1',
            'description': 'A web application built with Django and React.',
            'technologies': ['Django', 'React', 'MYSQL'],
            'link': 'https://github.com/yourusername/project1'
        },
        {
            'title': 'Project 2',
            'description': 'An e-commerce platform with payment integration.',
            'technologies': ['Django', 'Stripe', 'Bootstrap'],
            'link': 'https://github.com/yourusername/project2'
        }
    ],
    'contact': {
        'email': 'your.email@example.com',
        'linkedin': 'https://linkedin.com/in/yourusername',
        'github': 'https://github.com/yourusername'
    },
    'services': [
        {
            'icon': 'web',
            'title': 'Web Development',
            'description': 'Building responsive and scalable web applications tailored to your business needs.'
        },
        {
            'icon': 'design_services',
            'title': 'UI/UX Design',
            'description': 'Designing intuitive and engaging user interfaces for optimal user experience.'
        },
        {
            'icon': 'security',
            'title': 'Security Consulting',
            'description': 'Ensuring your applications are secure and follow best practices.'
        }
    ],
    'experience': [
        {
            'role': 'Senior Web Developer',
            'company': 'Tech Solutions Inc.',
            'period': '2021 - Present',
            'description': 'Lead developer for multiple client projects, focusing on full-stack development and cloud deployment.'
        },
        {
            'role': 'Frontend Developer',
            'company': 'Creative Minds Agency',
            'period': '2018 - 2021',
            'description': 'Developed interactive and modern web interfaces using React and Vue.'
        }
    ],
    'education': [
        {
            'degree': 'B.Sc. in Computer Science',
            'institution': 'State University',
            'period': '2014 - 2018',
            'description': 'Graduated with honors, specialized in software engineering.'
        },
        {
            'degree': 'Certified Django Developer',
            'institution': 'Django Software Foundation',
            'period': '2019',
            'description': 'Completed advanced Django certification.'
        }
    ],
    'testimonials': [
        {
            'quote': 'A highly skilled developer who delivers quality work on time.',
            'author': 'Jane Smith',
            'role': 'Project Manager, Tech Solutions Inc.'
        },
        {
            'quote': 'Creative, reliable, and always up-to-date with the latest technologies.',
            'author': 'Michael Lee',
            'role': 'CEO, Creative Minds Agency'
        }
    ],
    'blog_posts': [
        {
            'title': '5 Tips for Building Scalable Web Apps',
            'summary': 'Discover essential strategies for developing scalable and maintainable web applications.',
            'link': 'https://yourblog.com/scalable-web-apps'
        },
        {
            'title': 'Why UI/UX Matters in Modern Web Design',
            'summary': 'Explore the importance of user experience and interface design in today\'s digital landscape.',
            'link': 'https://yourblog.com/ui-ux-importance'
        }
    ]
}

def home(request):
    return render(request, 'portfolio/home.html', portfolio_content)