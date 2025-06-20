from django.shortcuts import render

# Dictionary to store portfolio content
portfolio_content = {
    'about': {
        'name': 'Juby Neil Valiao',
        'title': 'Web Developer',
        'bio': 'Passionate web developer with expertise in creating modern web applications.',
        'skills': ['Python', 'Django', 'PHP', 'Laravel', 'JavaScript', 'HTML/CSS', 'Java', 'MYSQL'],
        'tagline': 'Transforming ideas into exceptional digital experiences',
        'journey': {
            'title': 'My Journey',
            'sections': [
                {
                    'subtitle': 'Professional Background',
                    'content': "I'm a fresh graduate with a passion for web development and creating modern, responsive web applications. My journey in tech began with a curiosity about how websites work during my academic years, where I developed foundational skills through coursework and personal projects. I'm eager to apply my knowledge and grow as a professional developer."
                },
                {
                    'subtitle': 'Technical Expertise',
                    'content': "My core expertise lies in full-stack development with Python/Django and PHP/Laravel frameworks. I have experience building applications using Java with Netbeans IDE. I believe in writing clean, maintainable code and staying current with emerging technologies. I'm particularly interested in creating accessible interfaces that provide exceptional user experiences across all devices."
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
            'technologies': ['Django', 'HTML', 'CSS', 'Javascript'],
            'link': 'https://github.com/xf00889/portfolio'
        },
        {
            'title': 'NORSU Alumni Web Portal ',
            'description': 'A robust and feature-rich platform for Negros Oriental State University (NORSU) alumni to network, engage, and share information. ',
            'technologies': ['Django', 'HTML', 'Bootstrap','Javascript'],
            'link': 'https://github.com/xf00889/alumnisystem'
        },
        {
            'title': 'CTTMO Traffic Violation Management System  ',
            'description': 'Developed a web-based application for managing traffic violations, including recording infringement details and fines.',
            'technologies': ['Django', 'HTML', 'Bootstrap','Javascript'],
            'link': 'https://github.com/xf00889/CTTMO-Traffic-violation-Management-System'
        },
        {
            'title': 'Pharmacy Inventory Management System',
            'description': 'Built a multi user desktop app with role-based dashboards for inventory, prescription, stock, and sales management (POS).',
            'technologies': ['JAVA Netbeans', 'MYSQL', 'JavaFX'],
            'link': 'https://github.com/xf00889/pharmacy_inventory_management_system'
        },
        {
            'title': 'CRUD To Do List with Email Updates',
            'description': 'Created a web-based CRUD application for task tracking, featuring email notifications on task creation, updates, or deadlines.',
            'technologies': ['PHP', 'MYSQL', 'HTML', 'CSS', 'Javascript'],
            'link': 'https://github.com/xf00889/CRUD_TODOLIST_EMAIL_UPDATE'
        },
        {
            'title': 'Django Payroll Management System with QR & Face Recognition',
            'description': 'Developed a web-based payroll and attendance system using QR codes for staff authentication and payroll automation',
            'technologies': ['Django', 'HTML', 'Bootstrap','Javascript'],
            'link': 'https://github.com/xf00889/django_payrollMS_with_QR_and_facerecognition'
        }
    ],
    'contact': {
        'email': 'hutchiejn@gmail.com',
        'linkedin': 'https://www.linkedin.com/in/juby-neil-valiao-084b40237//',
        'github': 'https://github.com/xf00889',
        'facebook': 'https://www.facebook.com/jubyneil.valiao.7/',  
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
            'role': 'Intern',
            'company': 'NORSU-BSC',
            'period': 'July 2024 - March 2025',
            'description': '•	Supported staff members in their daily tasks, reducing workload burdens and allowing for increased focus on higher-priority assignments. Developed projects based on the office’s requirements and needs.'
        },
        {
            'role': 'Full Stack Developer',
            'company': 'Freelance',
            'period': 'February 2025 - Present',
            'description': 'Developing interactive and modern web interfaces using Django.'
        },
        # {
        #     'role': 'Backend Developer',
        #     'company': 'Digital Innovations Lab',
        #     'period': '2016 - 2018',
        #     'description': 'Developed and maintained RESTful APIs using Django and PostgreSQL. Implemented real-time features using WebSockets.'
        # },
        # {
        #     'role': 'Web Development Intern',
        #     'company': 'StartUp Hub',
        #     'period': '2015 - 2016',
        #     'description': 'Assisted in developing and testing web applications. Gained hands-on experience with modern web technologies.'
        # }
    ],
    'education': [
        {
            'degree': 'B.S. in Information Technology',
            'institution': 'Negros Oriental State University – BSC ( Tertiary Education)',
            'period': 'August 2020 - July 2025',
            'description': 'Graduated with Proficiency in Desktop Application Development'
        },
        {
            'degree': 'General Academic Strand',
            'institution': 'Miguel L. Daclan National High School (Secondary Education)',
            'period': 'June 2016 – April 2018',
            'description': 'Graduated with Honors'
        },
          {
            'degree': '',
            'institution': 'Vicente Z. Badon Campus (Secondary Education )',
            'period': 'June 2012 – April 2016',
            'description': 'Graduated as Salutatorian'
        },
        {
            'degree': '',
            'institution': 'Bongalonan Elementary School (Elementary Education)',
            'period': 'June 2008 – April 2012',
            'description': 'Graduated as Valedictorian'
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
            'icon': 'sports_tennis',
            'title': 'Badminton',
            'description': 'I love playing badminton in my free time. It helps me stay physically active and is a great way to socialize while enjoying a competitive sport.'
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
        'copyright': '© 2025 {{ about.name }}. All Rights Reserved.'
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
