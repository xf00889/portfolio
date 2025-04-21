from django.shortcuts import render

# Dictionary to store portfolio content
portfolio_content = {
    'about': {
        'name': 'Neil Micho Valiao',
        'title': 'Web Developer',
        'bio': 'Passionate web developer with expertise in creating modern web applications.',
        'skills': ['Python', 'Django', 'JavaScript', 'HTML/CSS', 'React', 'SQL'],
        'tagline': 'Transforming ideas into exceptional digital experiences',
        'journey': {
            'title': 'My Journey',
            'sections': [
                {
                    'subtitle': 'Professional Background',
                    'content': "I'm a passionate web developer with over 5 years of experience crafting modern, responsive web applications. My journey in tech began with a curiosity about how websites work, which quickly evolved into a career building digital solutions that solve real-world problems."
                },
                {
                    'subtitle': 'Technical Expertise',
                    'content': "My core expertise lies in full-stack development with Django and React. I believe in writing clean, maintainable code and staying current with emerging technologies. I'm particularly interested in creating accessible interfaces that provide exceptional user experiences across all devices."
                },
                {
                    'subtitle': 'Philosophy & Approach',
                    'content': "I approach each project with a problem-solving mindset, focusing on both technical excellence and business objectives. I value collaboration, continuous learning, and attention to detail. My goal is always to exceed expectations and deliver solutions that make a meaningful impact."
                }
            ]
        }
    },
    'projects': [
        {
            'title': 'Portfolio Website',
            'description': 'A web application built with Django and React.',
            'technologies': ['Django', 'React', 'MYSQL'],
            'link': 'https://github.com/yourusername/project1'
        },
        {
            'title': 'E-Commerce Platform',
            'description': 'An e-commerce platform with payment integration.',
            'technologies': ['Django', 'Stripe', 'Bootstrap'],
            'link': 'https://github.com/yourusername/project2'
        }
    ],
    'contact': {
        'email': 'neilmichovaliao@gmail.com',
        'linkedin': 'https://linkedin.com/in/micho',
        'github': 'https://github.com/xf00889',
        'title': 'Get In Touch'
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
            'description': 'Lead developer for multiple client projects, focusing on full-stack development and cloud deployment. Implemented CI/CD pipelines and mentored junior developers.'
        },
        {
            'role': 'Frontend Developer',
            'company': 'Creative Minds Agency',
            'period': '2018 - 2021',
            'description': 'Developed interactive and modern web interfaces using React and Vue. Improved site performance by 40% through optimization techniques.'
        },
        {
            'role': 'Backend Developer',
            'company': 'Digital Innovations Lab',
            'period': '2016 - 2018',
            'description': 'Developed and maintained RESTful APIs using Django and PostgreSQL. Implemented real-time features using WebSockets.'
        },
        {
            'role': 'Web Development Intern',
            'company': 'StartUp Hub',
            'period': '2015 - 2016',
            'description': 'Assisted in developing and testing web applications. Gained hands-on experience with modern web technologies.'
        }
    ],
    'education': [
        {
            'degree': 'B.Sc. in Information Technology',
            'institution': 'Negros Oriental State University',
            'period': '2014 - 2018',
            'description': 'Graduated with depression'
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
    ],
    'hobbies': [
        {
            'icon': 'sports_esports',
            'title': 'Gaming',
            'description': 'I enjoy playing strategy and role-playing games in my free time. Gaming helps me relax while also exercising problem-solving skills.'
        },
        {
            'icon': 'menu_book',
            'title': 'Reading',
            'description': 'I\'m an avid reader of science fiction, technology books, and philosophical works. Reading broadens my perspective and fuels my creativity.'
        },
        {
            'icon': 'hiking',
            'title': 'Hiking',
            'description': 'I love exploring nature trails and mountains. Hiking helps me stay physically active and connect with nature while clearing my mind.'
        }
    ],
    'section_titles': {
        'about': 'About Me',
        'services': 'Services',
        'experience': 'Experience',
        'education': 'Education',
        'projects': 'Projects',
        'hobbies': 'Hobbies & Interests',
        'contact': 'Contact'
    },
    'footer': {
        'message': 'Thank you for visiting my portfolio. I\'m always open to discussing new projects, creative ideas or opportunities to be part of your vision.',
        'copyright': '© 2023 {{ about.name }}. All Rights Reserved.'
    },
    'contact_form': {
        'title': 'Send Me a Message',
        'name_label': 'Name',
        'email_label': 'Email',
        'message_label': 'Message',
        'button_text': 'Send Message'
    }
}

def home(request):
    return render(request, 'portfolio/home.html', portfolio_content)
