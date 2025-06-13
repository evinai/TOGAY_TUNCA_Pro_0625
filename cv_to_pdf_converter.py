#!/usr/bin/env python3
"""
CV to PDF Converter - WeasyPrint only
--------------------------------------
This script converts your HTML CV to PDF using WeasyPrint.

Requirements:
- WeasyPrint: pip install weasyprint
"""

import os
import sys
from pathlib import Path


def check_requirements():
    """Check if required libraries are installed"""
    try:
        import weasyprint  # noqa: F401

        return True
    except ImportError:
        print("Missing required library: WeasyPrint")
        print("Please install it: pip install weasyprint")
        return False


def convert_with_weasyprint(html_file, output_file, css_file=None):
    """Convert HTML to PDF using WeasyPrint with options for page fitting"""
    from weasyprint import HTML, CSS

    print(f"Converting with WeasyPrint: {output_file}")

    # Create base URL for handling relative paths
    base_url = Path(html_file).parent.as_uri()

    # Load HTML
    html = HTML(filename=html_file, base_url=base_url)

    stylesheets = []

    # Add custom CSS if provided
    if css_file and os.path.exists(css_file):
        stylesheets.append(CSS(filename=css_file))

    # Add minimal CSS for optimization only (no margins or scaling)
    fit_css = CSS(
        string="""
        /* Space optimizations only - margins and scaling controlled by HTML */
        .section-title { margin-top: 15px !important; }
        .job-section { margin-bottom: 10px !important; }
        ul { 
            margin-top: 0px !important; 
            margin-bottom: 3px !important;
            padding-left: 15px !important;
        }
        li { margin-bottom: 2px !important; }
        
        /* Hide images in PDF generation */
        img { display: none !important; }
        """
    )

    stylesheets.append(fit_css)

    # Generate PDF
    html.write_pdf(
        output_file,
        stylesheets=stylesheets,
        presentational_hints=True,
        optimize_size=("fonts", "images"),
    )

    print(f"✅ WeasyPrint PDF created: {output_file}")


def main():
    """Main function to handle command-line usage"""
    if not check_requirements():
        return

    # Check for help flag
    if len(sys.argv) > 1 and sys.argv[1] in ["--help", "-h"]:
        print("CV to PDF Converter")
        print("------------------")
        print("Options:")
        print("  No arguments: Convert English CV")
        print("  --turkish: Convert Turkish CV")
        print("  --english-v4: Convert English CV v4")
        print("  --turkish-v4: Convert Turkish CV v4")
        print("  --english-v5: Convert English CV v5")
        print("  --turkish-v5: Convert Turkish CV v5")
        print("  --article1: Convert English Article 1")
        print("  --article1-turkish: Convert Turkish Article 1")
        print("  --article2: Convert English Article 2")
        print("  --article2-turkish: Convert Turkish Article 2")
        print("  --article3: Convert English Article 3")
        print("  --article3-turkish: Convert Turkish Article 3")
        print("  <filename.html>: Convert specific HTML file")
        print("  --all: Convert all HTML files to PDFs")
        print("------------------")
        return

    # Paths
    base_dir = "/home/evinai/Desktop/TOGAY_TUNCA_Pro_0625"

    # Check for arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "--turkish":
            html_file = os.path.join(base_dir, "cv_word_turkish_v2_educator.html")
            output_file = os.path.join(
                base_dir, "Togay_Tunca_CV_Turkish_Educator_WeasyPrint.pdf"
            )
        elif arg == "--english-v4":
            html_file = os.path.join(base_dir, "cv_word_english_v4_educator.html")
            output_file = os.path.join(
                base_dir, "Togay_Tunca_CV_English_v4_Educator_WeasyPrint.pdf"
            )
        elif arg == "--turkish-v4":
            html_file = os.path.join(base_dir, "cv_word_turkish_v4_educator.html")
            output_file = os.path.join(
                base_dir, "Togay_Tunca_CV_Turkish_v4_Educator_WeasyPrint.pdf"
            )
        elif arg == "--english-v5":
            html_file = os.path.join(base_dir, "cv_word_english_v5_educator.html")
            output_file = os.path.join(
                base_dir, "Togay_Tunca_CV_English_v5_Educator_WeasyPrint.pdf"
            )
        elif arg == "--turkish-v5":
            html_file = os.path.join(base_dir, "cv_word_turkish_v5_educator.html")
            output_file = os.path.join(
                base_dir, "Togay_Tunca_CV_Turkish_v5_Educator_WeasyPrint.pdf"
            )
        elif arg == "--article1":
            html_file = os.path.join(
                base_dir, "Article1_Education_Evolution_AI_Partnership.html"
            )
            output_file = os.path.join(
                base_dir, "Article1_Education_Evolution_AI_Partnership.pdf"
            )
        elif arg == "--article1-turkish":
            html_file = os.path.join(
                base_dir, "Article1_Education_Evolution_AI_Partnership_Turkish.html"
            )
            output_file = os.path.join(
                base_dir, "Article1_Education_Evolution_AI_Partnership_Turkish.pdf"
            )
        elif arg == "--article2":
            html_file = os.path.join(base_dir, "Article2_Where_to_Start_with_AI.html")
            output_file = os.path.join(base_dir, "Article2_Where_to_Start_with_AI.pdf")
        elif arg == "--article2-turkish":
            html_file = os.path.join(
                base_dir, "Article2_Where_to_Start_with_AI_Turkish.html"
            )
            output_file = os.path.join(
                base_dir, "Article2_Where_to_Start_with_AI_Turkish.pdf"
            )
        elif arg == "--article3":
            html_file = os.path.join(
                base_dir, "Article3_WhiteCollar_Workers_AI_Adaptation.html"
            )
            output_file = os.path.join(
                base_dir, "Article3_WhiteCollar_Workers_AI_Adaptation.pdf"
            )
        elif arg == "--article3-turkish":
            html_file = os.path.join(
                base_dir, "Article3_WhiteCollar_Workers_AI_Adaptation_Turkish.html"
            )
            output_file = os.path.join(
                base_dir, "Article3_WhiteCollar_Workers_AI_Adaptation_Turkish.pdf"
            )
        elif arg == "--all":
            # Convert all HTML files
            print("Converting all HTML files to PDFs...")

            # Define files to convert
            files_to_convert = [
                (
                    "cv_word_english_v2_educator.html",
                    "Togay_Tunca_CV_Educator_WeasyPrint.pdf",
                ),
                (
                    "cv_word_turkish_v2_educator.html",
                    "Togay_Tunca_CV_Educator_TR_WeasyPrint.pdf",
                ),
                (
                    "cv_word_english_v4_educator.html",
                    "Togay_Tunca_CV_English_v4_Educator_WeasyPrint.pdf",
                ),
                (
                    "cv_word_turkish_v4_educator.html",
                    "Togay_Tunca_CV_Turkish_v4_Educator_WeasyPrint.pdf",
                ),
                (
                    "cv_word_english_v5_educator.html",
                    "Togay_Tunca_CV_English_v5_Educator_WeasyPrint.pdf",
                ),
                (
                    "cv_word_turkish_v5_educator.html",
                    "Togay_Tunca_CV_Turkish_v5_Educator_WeasyPrint.pdf",
                ),
                (
                    "Article1_Education_Evolution_AI_Partnership.html",
                    "Article1_Education_Evolution_AI_Partnership.pdf",
                ),
                (
                    "Article1_Education_Evolution_AI_Partnership_Turkish.html",
                    "Article1_Education_Evolution_AI_Partnership_Turkish.pdf",
                ),
                (
                    "Article2_Where_to_Start_with_AI.html",
                    "Article2_Where_to_Start_with_AI.pdf",
                ),
                (
                    "Article2_Where_to_Start_with_AI_Turkish.html",
                    "Article2_Where_to_Start_with_AI_Turkish.pdf",
                ),
                (
                    "Article3_WhiteCollar_Workers_AI_Adaptation.html",
                    "Article3_WhiteCollar_Workers_AI_Adaptation.pdf",
                ),
                (
                    "Article3_WhiteCollar_Workers_AI_Adaptation_Turkish.html",
                    "Article3_WhiteCollar_Workers_AI_Adaptation_Turkish.pdf",
                ),
            ]

            for html_name, pdf_name in files_to_convert:
                input_file = os.path.join(base_dir, html_name)
                output = os.path.join(base_dir, pdf_name)

                if os.path.exists(input_file):
                    try:
                        convert_with_weasyprint(
                            input_file, output, os.path.join(base_dir, "pdf_styles.css")
                        )
                    except Exception as e:
                        print(f"Error converting {html_name}: {str(e)}")
                else:
                    print(f"File not found: {input_file}")

            print("\n✅ Batch conversion complete!")
            return

        elif sys.argv[1].endswith(".html"):
            # Direct file path provided
            html_file = (
                sys.argv[1]
                if os.path.isabs(sys.argv[1])
                else os.path.join(base_dir, sys.argv[1])
            )
            # Determine output name based on input file
            basename = os.path.basename(html_file)
            output_name = os.path.splitext(basename)[0] + ".pdf"
            output_file = os.path.join(base_dir, output_name)
        else:
            print("Invalid argument. Use --help for usage information.")
            return
    else:
        # Default to English
        html_file = os.path.join(base_dir, "cv_word_english_v2_educator.html")
        output_file = os.path.join(base_dir, "Togay_Tunca_CV_Educator_WeasyPrint.pdf")

    css_file = os.path.join(base_dir, "pdf_styles.css")

    # Check if HTML file exists
    if not os.path.exists(html_file):
        print(f"Error: Could not find HTML file: {html_file}")
        return

    # Convert to PDF
    convert_with_weasyprint(html_file, output_file, css_file)

    print("\n✅ PDF conversion complete!")
    print(f"Output: {os.path.basename(output_file)}")


if __name__ == "__main__":
    main()
