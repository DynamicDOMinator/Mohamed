# -*- coding: utf-8 -*-
"""
Generator for the Elegant Arabic Wedding Invitation Website
Updated with exact user instructions:
1. No gradient colors (100% solid colors).
2. Remove Mohamed & Rojain from every page except the initial invitation badge and the invitation itself.
3. Merge first 2 pages as specified:
   - بسم الله الرحمن الرحيم
   - نتشرف بدعوتكم لحضور حفل عقد قران
   - stacked: محمد
   - stacked: على كريمة السيد وائل
   - stacked: روجين
   - متمنين أن / بقلوب يملؤها الفرح ...etc
   - with the interactive invitation envelope embedded seamlessly.
4. Make the "عرض تفاصيل" button smaller.
5. Include more but subtle floral textures throughout the website.
6. Details page: text & frame smaller, remove footer text "صورة المسجد ..etc".
7. Timing not in frames but as full time in single line, and remove the paragraph of the details page.
"""

html_content = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#4a0e17">
  <title>دعوة عقد قران | محمد & روجين</title>

  <!-- Google Fonts: Aref Ruqaa for majestic names, Amiri for sacred texts, Alexandria for editorial body -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Alexandria:wght@300;400;500;600;700&family=Amiri:ital,wght@0,400;0,700;1,400&family=Aref+Ruqaa:wght@400;700&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================
       DESIGN SYSTEM: SOLID EDITORIAL LUXURY (NO GRADIENTS)
       Palette extracted from reference image:
       - Deep Royal Burgundy: #4a0e17, #58141f, #38070e
       - Warm Ivory & Paper: #faf7f2, #fdfcf9, #f5efe6
       - Champagne Gold: #c5a059, #b88d4c, #8a6829
       - Text: #231417, #453034, #6e575c
       ========================================================== */
    :root {
      --burgundy-deep: #38070e;
      --burgundy-main: #4a0e17;
      --burgundy-rich: #58141f;
      --burgundy-wine: #6e1d2a;
      --burgundy-light: #8e2b3c;
      --burgundy-tint: #f6eef0;

      --ivory-base: #faf7f2;
      --ivory-paper: #fdfcf9;
      --ivory-card: #f8f4ec;
      --champagne-tint: #f3ebdc;
      --champagne-gold: #c5a059;
      --champagne-bright: #d4af37;
      --gold-deep: #7d5e2a;

      --text-main: #231417;
      --text-editorial: #453034;
      --text-muted: #6e575c;
      --text-light: #947e83;

      --border-subtle: #ebdcc4;
      --border-medium: #c5a059;
      --border-burgundy: #4a0e17;

      --shadow-soft: 0 8px 24px rgba(58, 10, 17, 0.05);
      --shadow-card: 0 14px 40px rgba(58, 10, 17, 0.07);
      --shadow-deep: 0 20px 55px rgba(58, 10, 17, 0.12);

      --font-names: 'Aref Ruqaa', 'Amiri', serif;
      --font-calligraphy: 'Amiri', serif;
      --font-body: 'Alexandria', 'Amiri', sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    html {
      scroll-behavior: smooth;
      background-color: var(--ivory-base);
      color: var(--text-main);
    }

    /* Subtle Botanical & Floral Textures Pattern on Body */
    body {
      font-family: var(--font-body);
      background-color: var(--ivory-base);
      background-image: 
        url("data:image/svg+xml,%3Csvg width='80' height='80' viewBox='0 0 80 80' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23c5a059' fill-opacity='0.045' fill-rule='evenodd'%3E%3Cpath d='M40 0C40 22.091 22.091 40 0 40C22.091 40 40 57.909 40 80C40 57.909 57.909 40 80 40C57.909 40 40 22.091 40 0Z M40 32C44.418 32 48 35.582 48 40C48 44.418 44.418 48 40 48C35.582 48 32 44.418 32 40C32 35.582 35.582 32 40 32Z'/%3E%3Ccircle cx='40' cy='15' r='2'/%3E%3Ccircle cx='40' cy='65' r='2'/%3E%3Ccircle cx='15' cy='40' r='2'/%3E%3Ccircle cx='65' cy='40' r='2'/%3E%3C/g%3E%3C/svg%3E");
      line-height: 1.9;
      font-size: 16px;
      overflow-x: hidden;
      position: relative;
    }

    ::selection {
      background: var(--champagne-tint);
      color: var(--burgundy-deep);
    }

    a {
      text-decoration: none;
      color: inherit;
    }

    button {
      font-family: inherit;
      border: none;
      background: none;
      cursor: pointer;
    }

    /* Container */
    .container {
      width: min(100% - 36px, 840px);
      margin-inline: auto;
      position: relative;
      z-index: 2;
    }

    .container-compact {
      width: min(100% - 36px, 580px);
      margin-inline: auto;
      position: relative;
      z-index: 2;
    }

    /* Solid Framing Lines (No Gradients) */
    .luxury-frame-line {
      position: fixed;
      left: 0;
      right: 0;
      height: 3px;
      z-index: 999;
      pointer-events: none;
      background-color: var(--burgundy-main);
    }
    .frame-line-top { top: 0; border-bottom: 1px solid var(--champagne-gold); }
    .frame-line-bottom { bottom: 0; border-top: 1px solid var(--champagne-gold); }

    /* Top Floating Utility Controls */
    .floating-nav {
      position: fixed;
      top: 18px;
      left: 18px;
      display: flex;
      gap: 10px;
      z-index: 100;
    }

    .pill-btn {
      background-color: var(--ivory-paper);
      border: 1px solid var(--border-medium);
      border-radius: 30px;
      padding: 6px 14px;
      font-size: 13px;
      color: var(--burgundy-main);
      display: inline-flex;
      align-items: center;
      gap: 7px;
      box-shadow: var(--shadow-soft);
      transition: all 0.3s ease;
      cursor: pointer;
    }

    .pill-btn:hover {
      background-color: #ffffff;
      border-color: var(--burgundy-main);
      transform: translateY(-2px);
      box-shadow: 0 4px 14px rgba(74, 14, 23, 0.12);
    }

    .pill-btn.active {
      background-color: var(--burgundy-main);
      color: #ffffff;
      border-color: var(--burgundy-main);
    }

    /* Petals canvas */
    #petalsCanvas {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 1;
    }

    /* Section Styling */
    .section {
      position: relative;
      padding: 85px 18px;
      text-align: center;
    }

    .section-cream {
      background-color: var(--ivory-card);
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
    }

    /* Section Headers */
    .section-crest {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      margin-bottom: 14px;
      color: var(--champagne-gold);
    }

    .crest-line {
      width: 40px;
      height: 1px;
      background-color: var(--champagne-gold);
    }

    .crest-symbol {
      font-size: 15px;
      color: var(--champagne-gold);
      letter-spacing: 2px;
    }

    .section-title {
      font-family: var(--font-names);
      font-size: clamp(28px, 5.5vw, 40px);
      font-weight: 400;
      color: var(--burgundy-deep);
      margin-bottom: 8px;
      letter-spacing: -0.5px;
    }

    .section-subtitle {
      font-size: 15px;
      color: var(--text-muted);
      max-width: 500px;
      margin: 0 auto 35px;
      line-height: 1.8;
      font-weight: 400;
    }

    /* Flourish & Dividers (Solid) */
    .divider-flourish {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      margin: 24px auto;
      max-width: 220px;
      color: var(--champagne-gold);
      opacity: 0.9;
    }

    .divider-flourish::before,
    .divider-flourish::after {
      content: "";
      flex: 1;
      height: 1px;
      background-color: var(--champagne-gold);
      opacity: 0.5;
    }

    /* ==========================================================
       MERGED OPENING & INVITATION SECTION
       Strictly structured as requested:
       - بسم الله الرحمن الرحيم
       - نتشرف بدعوتكم لحضور حفل عقد قران
       - stacked: محمد
       - stacked: على كريمة السيد وائل
       - stacked: روجين
       - بقلوب يملؤها الفرح والسرور...
       - بارك الله لهما...
       - Followed seamlessly by the unfolding invitation card!
       ========================================================== */
    .merged-opening-section {
      padding: 70px 18px 85px;
      position: relative;
      text-align: center;
      background-color: var(--ivory-base);
    }

    .master-invitation-card {
      max-width: 740px;
      width: 100%;
      margin: 0 auto;
      padding: 55px 35px 50px;
      background-color: #ffffff;
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      box-shadow: 
        0 20px 50px rgba(74, 14, 23, 0.06),
        inset 0 0 0 6px #ffffff,
        inset 0 0 0 7.5px var(--border-subtle);
      position: relative;
    }

    /* Subtle Botanical Corner Linework */
    .corner-floral-filigree {
      position: absolute;
      width: 36px;
      height: 36px;
      color: var(--champagne-gold);
      pointer-events: none;
      opacity: 0.8;
    }
    .filigree-tr { top: 12px; right: 12px; }
    .filigree-tl { top: 12px; left: 12px; transform: scaleX(-1); }
    .filigree-br { bottom: 12px; right: 12px; transform: scaleY(-1); }
    .filigree-bl { bottom: 12px; left: 12px; transform: scale(-1); }

    /* Subtle Botanical Background Watermark */
    .card-floral-watermark {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 340px;
      height: 340px;
      pointer-events: none;
      opacity: 0.04;
      color: var(--burgundy-main);
    }

    /* Monogram Crest */
    .monogram-seal-box {
      margin-bottom: 22px;
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
    }

    .monogram-seal-badge {
      width: 62px;
      height: 62px;
      border-radius: 50%;
      background-color: var(--burgundy-main);
      border: 2px solid var(--champagne-gold);
      box-shadow: 0 4px 15px rgba(74, 14, 23, 0.22);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--champagne-bright);
      font-family: var(--font-names);
      font-size: 24px;
      letter-spacing: 1px;
    }

    /* 1. Basmala */
    .bismillah-text {
      font-family: var(--font-calligraphy);
      font-size: clamp(23px, 4.8vw, 30px);
      color: var(--burgundy-rich);
      margin: 0 0 20px;
      font-weight: 700;
      letter-spacing: 0.5px;
    }

    /* 2. Invitation Greeting Phrase */
    .invitation-honor-phrase {
      font-size: clamp(17px, 3.5vw, 20px);
      color: var(--text-editorial);
      line-height: 2;
      margin-bottom: 24px;
      font-weight: 500;
    }

    /* 3. Stacked Names Block */
    .stacked-names-flow {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      margin: 10px auto 26px;
      padding: 18px 24px;
      background-color: var(--ivory-card);
      border-top: 1px solid var(--border-medium);
      border-bottom: 1px solid var(--border-medium);
      border-radius: 4px;
      max-width: 520px;
    }

    .stacked-name-groom {
      font-family: var(--font-names);
      font-size: clamp(48px, 9.5vw, 76px);
      color: var(--burgundy-main);
      line-height: 1.2;
      font-weight: 700;
      letter-spacing: -0.5px;
    }

    .stacked-bridge-phrase {
      font-size: clamp(17px, 3.4vw, 21px);
      color: var(--text-editorial);
      font-weight: 500;
      margin: 4px 0;
    }

    .stacked-name-bride {
      font-family: var(--font-names);
      font-size: clamp(48px, 9.5vw, 76px);
      color: var(--burgundy-main);
      line-height: 1.2;
      font-weight: 700;
      letter-spacing: -0.5px;
    }

    /* 4. Warm Welcoming Message */
    .heartfelt-body-text {
      font-size: clamp(16px, 3.2vw, 18.5px);
      color: var(--text-muted);
      line-height: 2.1;
      max-width: 560px;
      margin: 18px auto 22px;
      font-weight: 400;
    }

    /* 5. Prophetic Dua */
    .prophetic-dua-badge {
      display: inline-block;
      padding: 12px 26px;
      background-color: #ffffff;
      border: 1px solid var(--champagne-gold);
      border-radius: 40px;
      box-shadow: var(--shadow-soft);
      margin: 8px 0 35px;
    }

    .prophetic-dua-content {
      font-family: var(--font-calligraphy);
      font-size: clamp(17px, 3.5vw, 21px);
      color: var(--burgundy-rich);
      font-weight: 700;
      letter-spacing: 0.3px;
    }

    /* ==========================================================
       SEAMLESS INTERACTIVE INVITATION CARD (UNFOLDING FOLIO)
       Embedded right inside the opening experience!
       ========================================================== */
    .interactive-folio-wrapper {
      max-width: 560px;
      margin: 20px auto 10px;
      perspective: 1400px;
      position: relative;
      text-align: center;
    }

    .burgundy-folio-envelope {
      width: 100%;
      position: relative;
      border-radius: 6px;
      box-shadow: 0 18px 50px rgba(58, 10, 17, 0.2);
      transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
      overflow: visible;
      background-color: var(--burgundy-rich);
      background-image: url('assets/burgundy-envelope-ref.jpg');
      background-size: cover;
      background-position: center;
      border: 1px solid var(--champagne-gold);
      min-height: 420px;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
    }

    /* 3D Diagonal Flaps Layer */
    .envelope-flaps-layer {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 15;
    }

    .top-triangle-flap {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 220px;
      transform-origin: top center;
      transform-style: preserve-3d;
      transition: transform 1.1s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 25;
      background-color: var(--burgundy-rich);
      background-image: url('assets/burgundy-envelope-ref.jpg');
      background-size: cover;
      background-position: top center;
      clip-path: polygon(0 0, 100% 0, 50% 100%);
      border-bottom: 1px solid var(--champagne-gold);
      filter: drop-shadow(0 8px 18px rgba(35, 4, 8, 0.35));
    }

    .left-side-flap {
      position: absolute;
      top: 0;
      left: 0;
      bottom: 0;
      width: 55%;
      clip-path: polygon(0 0, 100% 50%, 0 100%);
      background-color: var(--burgundy-deep);
      background-image: url('assets/burgundy-envelope-ref.jpg');
      background-size: cover;
      background-position: left center;
      z-index: 18;
      border-right: 1px solid rgba(197, 160, 89, 0.3);
      transition: transform 0.8s ease;
    }

    .right-side-flap {
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      width: 55%;
      clip-path: polygon(100% 0, 0 50%, 100% 100%);
      background-color: var(--burgundy-deep);
      background-image: url('assets/burgundy-envelope-ref.jpg');
      background-size: cover;
      background-position: right center;
      z-index: 19;
      border-left: 1px solid rgba(197, 160, 89, 0.3);
      transition: transform 0.8s ease;
    }

    /* 3D Wax Seal with Monogram */
    .wax-seal-center-action {
      position: absolute;
      top: 190px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 35;
      cursor: pointer;
      transition: all 0.4s ease;
    }

    .wax-seal-center-action:hover {
      transform: translateX(-50%) scale(1.06);
    }

    .wax-seal-button-disc {
      width: 74px;
      height: 74px;
      border-radius: 50%;
      background-color: var(--burgundy-main);
      box-shadow: 
        0 8px 20px rgba(35, 4, 8, 0.5),
        inset 0 2px 4px rgba(255, 255, 255, 0.25);
      border: 2px solid var(--champagne-gold);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      position: relative;
    }

    .wax-seal-button-disc::before {
      content: "";
      position: absolute;
      inset: 4px;
      border-radius: 50%;
      border: 1px dashed rgba(197, 160, 89, 0.5);
      pointer-events: none;
    }

    .seal-monogram-text {
      font-family: var(--font-names);
      font-size: 26px;
      font-weight: 700;
      line-height: 1;
    }

    .seal-ribbon-tails {
      position: absolute;
      bottom: -18px;
      left: 50%;
      transform: translateX(-50%);
      width: 44px;
      height: 24px;
      display: flex;
      justify-content: center;
      gap: 5px;
      z-index: -1;
    }

    .ribbon-blade {
      width: 14px;
      height: 26px;
      background-color: var(--champagne-gold);
      clip-path: polygon(0 0, 100% 0, 100% 80%, 50% 100%, 0 80%);
      box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
    }
    .ribbon-blade.left { transform: rotate(15deg); }
    .ribbon-blade.right { transform: rotate(-15deg); }

    /* Open Prompt Pill */
    .unfold-pill-prompt {
      position: absolute;
      bottom: 22px;
      left: 50%;
      transform: translateX(-50%);
      background-color: #ffffff;
      border: 1px solid var(--champagne-gold);
      color: var(--burgundy-deep);
      padding: 8px 20px;
      border-radius: 30px;
      font-size: 14px;
      font-weight: 600;
      white-space: nowrap;
      box-shadow: 0 6px 20px rgba(45, 6, 12, 0.2);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      transition: all 0.3s ease;
      z-index: 30;
    }

    .unfold-pill-prompt:hover {
      background-color: var(--ivory-paper);
      border-color: var(--burgundy-main);
      color: var(--burgundy-main);
    }

    /* Inner Letterpress Card */
    .inner-unfolded-card {
      background-color: var(--ivory-paper);
      padding: 48px 30px 40px;
      border-radius: 4px;
      text-align: center;
      position: relative;
      z-index: 10;
      border: 1px solid var(--border-medium);
      box-shadow: 
        inset 0 0 0 6px #ffffff,
        inset 0 0 0 7.5px var(--border-subtle);
      transition: all 0.9s cubic-bezier(0.16, 1, 0.3, 1);
      opacity: 0.95;
    }

    .inner-card-flora-header {
      width: 120px;
      height: 28px;
      margin: 0 auto 12px;
      color: var(--champagne-gold);
    }

    .inner-card-occasion {
      font-family: var(--font-calligraphy);
      font-size: 19px;
      color: var(--champagne-gold);
      font-weight: 700;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
    }

    .inner-card-invitation-text {
      color: var(--text-editorial);
      font-size: 15.5px;
      line-height: 2;
      max-width: 440px;
      margin: 0 auto 18px;
    }

    /* SMALLER "عرض تفاصيل" BUTTON AS REQUESTED */
    .inner-card-button-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
      margin-top: 22px;
    }

    .btn-details-compact {
      background-color: var(--burgundy-main);
      color: #ffffff;
      padding: 8px 18px;
      border-radius: 4px;
      font-size: 13.5px;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border: 1px solid var(--burgundy-main);
      box-shadow: 0 4px 12px rgba(74, 14, 23, 0.18);
      transition: all 0.3s ease;
      cursor: pointer;
    }

    .btn-details-compact:hover {
      background-color: var(--burgundy-rich);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(74, 14, 23, 0.28);
    }

    .btn-fold-compact {
      background-color: transparent;
      color: var(--burgundy-main);
      padding: 8px 16px;
      border-radius: 4px;
      font-size: 13.5px;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border: 1px solid var(--border-medium);
      transition: all 0.3s ease;
      cursor: pointer;
    }

    .btn-fold-compact:hover {
      background-color: var(--ivory-card);
      border-color: var(--burgundy-main);
      transform: translateY(-2px);
    }

    /* OPENED STATE */
    .interactive-folio-wrapper.is-opened .top-triangle-flap {
      transform: rotateX(175deg);
      z-index: 5;
    }

    .interactive-folio-wrapper.is-opened .left-side-flap {
      transform: translateX(-35px) rotateY(-20deg);
      opacity: 0.15;
    }

    .interactive-folio-wrapper.is-opened .right-side-flap {
      transform: translateX(35px) rotateY(20deg);
      opacity: 0.15;
    }

    .interactive-folio-wrapper.is-opened .wax-seal-center-action {
      transform: translateX(-50%) translateY(-55px) scale(0.8);
      opacity: 0.2;
      pointer-events: none;
    }

    .interactive-folio-wrapper.is-opened .unfold-pill-prompt {
      opacity: 0;
      pointer-events: none;
      visibility: hidden;
    }

    .interactive-folio-wrapper.is-opened .inner-unfolded-card {
      transform: translateY(-10px);
      box-shadow: 
        0 20px 50px rgba(58, 10, 17, 0.15),
        inset 0 0 0 6px #ffffff,
        inset 0 0 0 7.5px var(--border-subtle);
      opacity: 1;
    }

    /* ==========================================================
       SECTION 2: WEDDING DETAILS & VENUE
       Smaller frame, smaller text, timing as full time in single line,
       removed paragraph, removed footer photo attribution.
       ========================================================== */
    .venue-compact-card {
      max-width: 580px;
      margin: 0 auto;
      background-color: var(--ivory-paper);
      border-radius: 6px;
      border: 1px solid var(--border-medium);
      box-shadow: var(--shadow-card);
      overflow: hidden;
      position: relative;
    }

    .venue-photo-compact-frame {
      position: relative;
      width: 100%;
      height: 220px;
      overflow: hidden;
      background-color: #2b1216;
    }

    .venue-photo-actual {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 38%;
      display: block;
      transition: transform 0.6s ease;
    }

    .venue-compact-card:hover .venue-photo-actual {
      transform: scale(1.03);
    }

    .venue-photo-badge {
      position: absolute;
      bottom: 14px;
      right: 18px;
      background-color: var(--ivory-paper);
      padding: 5px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
      color: var(--burgundy-deep);
      border: 1px solid var(--border-subtle);
      box-shadow: 0 3px 12px rgba(0, 0, 0, 0.15);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .mosque-metadata-compact-strip {
      background-color: var(--ivory-card);
      border-bottom: 1px solid var(--border-subtle);
      padding: 12px 18px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      text-align: right;
    }

    .mosque-metadata-text {
      font-size: 12.5px;
      color: var(--text-editorial);
      line-height: 1.5;
    }

    .mosque-rating-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: #ffffff;
      padding: 4px 10px;
      border-radius: 16px;
      border: 1px solid var(--border-subtle);
      font-size: 12px;
    }

    .rating-stars-solid {
      color: #e5b338;
      font-size: 13px;
      letter-spacing: 1px;
    }

    .rating-label {
      font-weight: 600;
      color: var(--burgundy-main);
    }

    .venue-compact-body {
      padding: 24px 20px 28px;
      text-align: center;
    }

    .venue-compact-title {
      font-family: var(--font-names);
      font-size: clamp(26px, 5vw, 34px);
      color: var(--burgundy-deep);
      margin-bottom: 4px;
      font-weight: 400;
    }

    .venue-compact-address {
      color: var(--text-muted);
      font-size: 14.5px;
      line-height: 1.6;
      margin-bottom: 20px;
    }

    /* FULL TIME & DATE IN A SINGLE LINE (NO FRAMES) AS REQUESTED */
    .timing-single-line-container {
      background-color: var(--ivory-card);
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      padding: 14px 18px;
      margin: 18px auto 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      color: var(--burgundy-deep);
      font-weight: 700;
      font-size: clamp(14.5px, 3.2vw, 16.5px);
    }

    .timing-icon-badge {
      color: var(--champagne-gold);
      font-size: 18px;
    }

    /* Google Maps Button (Solid) */
    .btn-maps-solid {
      background-color: var(--burgundy-main);
      color: #ffffff;
      padding: 11px 26px;
      border-radius: 4px;
      font-size: 14.5px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 15px rgba(74, 14, 23, 0.2);
      border: 1px solid var(--burgundy-main);
      transition: all 0.3s ease;
    }

    .btn-maps-solid:hover {
      background-color: var(--burgundy-rich);
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(74, 14, 23, 0.3);
      color: #ffffff;
    }

    .btn-maps-solid svg {
      width: 18px;
      height: 18px;
      color: var(--champagne-bright);
    }

    /* ==========================================================
       SECTION 3: ARABIC COUNTDOWN
       (No couple names here)
       ========================================================== */
    .countdown-cluster-row {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
      margin: 28px auto 20px;
      max-width: 580px;
      direction: rtl;
    }

    .time-capsule-box {
      flex: 1 1 110px;
      max-width: 130px;
      min-width: 95px;
      background-color: #ffffff;
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      padding: 18px 8px 14px;
      text-align: center;
      box-shadow: var(--shadow-soft);
      position: relative;
      transition: all 0.3s ease;
    }

    .time-capsule-box:hover {
      transform: translateY(-3px);
      border-color: var(--burgundy-main);
      box-shadow: var(--shadow-card);
    }

    .capsule-digit-text {
      font-family: var(--font-names);
      font-size: clamp(34px, 7vw, 48px);
      font-weight: 700;
      color: var(--burgundy-deep);
      line-height: 1.1;
      display: block;
      margin-bottom: 4px;
    }

    .capsule-unit-label {
      font-size: 13.5px;
      color: var(--text-muted);
      font-weight: 600;
      display: block;
    }

    .countdown-live-row {
      font-size: 14px;
      color: var(--burgundy-main);
      margin-top: 22px;
      font-weight: 500;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }

    .live-pulse-solid {
      width: 8px;
      height: 8px;
      background-color: var(--burgundy-light);
      border-radius: 50%;
    }

    /* ==========================================================
       SECTION 4: IMPORTANT NOTES
       (No couple names here)
       ========================================================== */
    .notes-compact-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      max-width: 680px;
      margin: 0 auto;
    }

    .note-card-box {
      background-color: #ffffff;
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      padding: 28px 22px;
      text-align: right;
      position: relative;
      box-shadow: var(--shadow-soft);
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .note-card-box:hover {
      transform: translateY(-2px);
      border-color: var(--burgundy-main);
      box-shadow: var(--shadow-card);
    }

    .note-top-header {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .note-icon-pod {
      width: 48px;
      height: 48px;
      border-radius: 10px;
      background-color: var(--ivory-card);
      border: 1px solid var(--border-medium);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .note-icon-pod svg {
      width: 32px;
      height: 32px;
    }

    .note-heading-title {
      font-family: var(--font-names);
      font-size: 21px;
      color: var(--burgundy-deep);
      font-weight: 400;
    }

    .note-paragraph {
      color: var(--text-editorial);
      font-size: 14.5px;
      line-height: 2;
      font-weight: 400;
    }

    /* ==========================================================
       SECTION 5: CLOSING SECTION
       Per instruction: Mohamed & Rojain removed from here!
       Solid elegant floral sign-off crest.
       ========================================================== */
    .closing-section-wrapper {
      padding: 95px 18px 85px;
      background-color: var(--ivory-base);
      text-align: center;
      position: relative;
    }

    .closing-content-card {
      max-width: 600px;
      margin: 0 auto;
      padding: 48px 30px;
      background-color: #ffffff;
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      box-shadow: var(--shadow-card);
      position: relative;
    }

    .closing-warm-headline {
      font-family: var(--font-names);
      font-size: clamp(32px, 6.5vw, 46px);
      color: var(--burgundy-deep);
      font-weight: 400;
      margin-bottom: 16px;
    }

    .closing-farewell-text {
      font-size: clamp(15.5px, 3vw, 18px);
      color: var(--text-editorial);
      line-height: 2.1;
      max-width: 500px;
      margin: 0 auto 24px;
    }

    .closing-floral-emblem {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin: 16px auto 0;
      color: var(--champagne-gold);
      font-size: 20px;
    }

    /* Footer */
    .editorial-footer-bar {
      padding: 30px 20px;
      text-align: center;
      background-color: var(--ivory-paper);
      border-top: 1px solid var(--border-subtle);
      color: var(--text-light);
      font-size: 13px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      align-items: center;
    }

    .footer-pills-cluster {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
      margin-bottom: 6px;
    }

    .footer-action-button {
      color: var(--burgundy-main);
      font-size: 12.5px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 16px;
      border: 1px solid var(--border-medium);
      border-radius: 20px;
      background-color: #ffffff;
      transition: all 0.25s ease;
    }

    .footer-action-button:hover {
      background-color: var(--ivory-card);
      border-color: var(--burgundy-main);
      color: var(--burgundy-deep);
      transform: translateY(-2px);
    }

    /* Responsiveness */
    @media (max-width: 768px) {
      .section {
        padding: 65px 14px;
      }

      .merged-opening-section {
        padding: 55px 12px 70px;
      }

      .master-invitation-card {
        padding: 40px 16px 36px;
      }

      .stacked-names-flow {
        padding: 14px 16px;
      }

      .notes-compact-grid {
        grid-template-columns: 1fr;
        gap: 16px;
      }

      .venue-photo-compact-frame {
        height: 190px;
      }

      .countdown-cluster-row {
        gap: 8px;
      }

      .time-capsule-box {
        flex: 1 1 calc(50% - 8px);
        max-width: none;
        padding: 14px 6px;
      }

      .capsule-digit-text {
        font-size: 34px;
      }

      .mosque-metadata-compact-strip {
        flex-direction: column;
        align-items: flex-start;
      }

      .floating-nav {
        top: 10px;
        left: 10px;
      }

      .pill-btn span.label-text {
        display: none;
      }
    }
  </style>
</head>
<body>

  <!-- Hidden SVG Symbols for soft botanical filigrees -->
  <svg style="display:none" aria-hidden="true">
    <symbol id="corner-filigree-flora" viewBox="0 0 40 40">
      <path fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"
        d="M2,38 L2,10 C2,5.6 5.6,2 10,2 L38,2 M6,34 L6,12 C6,8.7 8.7,6 12,6 L34,6 M10,10 L18,18" />
    </symbol>

    <symbol id="floral-center-ornament" viewBox="0 0 200 40">
      <path fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"
        d="M10,20 Q60,6 90,20 Q95,6 100,6 Q105,6 110,20 Q140,6 190,20 M100,6 L100,34 M85,20 C85,15 95,15 100,20 C105,15 115,15 115,20" />
      <circle cx="100" cy="6" r="2.5" fill="currentColor" />
      <circle cx="70" cy="18" r="1.5" fill="currentColor" />
      <circle cx="130" cy="18" r="1.5" fill="currentColor" />
    </symbol>

    <symbol id="botanical-watermark-symbol" viewBox="0 0 240 240">
      <path fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"
        d="M120,20 C140,60 180,90 220,120 C180,150 140,180 120,220 C100,180 60,150 20,120 C60,90 100,60 120,20 Z" />
      <circle cx="120" cy="120" r="30" fill="none" stroke="currentColor" stroke-width="1" />
      <circle cx="120" cy="120" r="10" fill="none" stroke="currentColor" stroke-width="1" />
    </symbol>
  </svg>

  <!-- Luxury Framing Lines (Solid) -->
  <div class="luxury-frame-line frame-line-top" aria-hidden="true"></div>
  <div class="luxury-frame-line frame-line-bottom" aria-hidden="true"></div>

  <!-- Ambient Audio & WhatsApp Share Floating Controls -->
  <nav class="floating-nav" aria-label="أدوات الصفحة">
    <button type="button" class="pill-btn" id="btnAmbientAudio" title="تشغيل / كتم نغمات هادئة">
      <span id="audioSymbol">♪</span>
      <span class="label-text" id="audioLabelText">نغمات هادئة</span>
    </button>
    <button type="button" class="pill-btn" id="btnShareWhatsApp" title="مشاركة الدعوة">
      <span>✉</span>
      <span class="label-text">مشاركة الدعوة</span>
    </button>
  </nav>

  <!-- Delicate Falling Petals Canvas -->
  <canvas id="petalsCanvas" aria-hidden="true"></canvas>

  <!-- ==========================================================
       MERGED FIRST 2 PAGES: OPENING & INTERACTIVE INVITATION
       Exact order specified by the user:
       - بسم الله الرحمن الرحيم
       - نتشرف بدعوتكم لحضور حفل عقد قران
       - stacked: محمد
       - stacked: على كريمة السيد وائل
       - stacked: روجين
       - بقلوب يملؤها الفرح والسرور، يسعدنا دعوتكم لتشاركونا أجمل لحظات العمر، بحضوركم تكتمل فرحتنا.
       - بارك الله لهما وبارك عليهما وجمع بينهما في خير
       - Followed by the unfolding invitation card!
       ========================================================== -->
  <main class="merged-opening-section" id="opening-invitation">
    <div class="master-invitation-card">

      <!-- Subtle Botanical Filigrees in Corners -->
      <svg class="corner-floral-filigree filigree-tr" aria-hidden="true"><use href="#corner-filigree-flora" /></svg>
      <svg class="corner-floral-filigree filigree-tl" aria-hidden="true"><use href="#corner-filigree-flora" /></svg>
      <svg class="corner-floral-filigree filigree-br" aria-hidden="true"><use href="#corner-filigree-flora" /></svg>
      <svg class="corner-floral-filigree filigree-bl" aria-hidden="true"><use href="#corner-filigree-flora" /></svg>

      <!-- Center Watermark Pattern -->
      <svg class="card-floral-watermark" aria-hidden="true"><use href="#botanical-watermark-symbol" /></svg>

      <!-- Royal Monogram Seal Badge -->
      <div class="monogram-seal-box">
        <div class="monogram-seal-badge" title="محمد & روجين">
          <span>م & ر</span>
        </div>
      </div>

      <!-- 1. Bismillah -->
      <p class="bismillah-text">
        بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
      </p>

      <!-- 2. Invitation Greeting -->
      <p class="invitation-honor-phrase">
        نتشرف بدعوتكم لحضور حفل عقد قران
      </p>

      <!-- 3. STACKED NAMES AS SPECIFIED -->
      <div class="stacked-names-flow">
        <h1 class="stacked-name-groom">محمد</h1>
        <p class="stacked-bridge-phrase">على كريمة السيد وائل</p>
        <h2 class="stacked-name-bride">روجين</h2>
      </div>

      <!-- Subtle Floral Divider -->
      <svg style="width:160px; height:28px; margin:0 auto 16px; color:var(--champagne-gold);" aria-hidden="true">
        <use href="#floral-center-ornament" />
      </svg>

      <!-- 4. Heartfelt Text -->
      <p class="heartfelt-body-text">
        بقلوب يملؤها الفرح والسرور، يسعدنا دعوتكم لتشاركونا أجمل لحظات العمر، بحضوركم تكتمل فرحتنا.
      </p>

      <!-- 5. Prophetic Dua -->
      <div class="prophetic-dua-badge">
        <span class="prophetic-dua-content">
          بارك الله لهما وبارك عليهما وجمع بينهما في خير
        </span>
      </div>

      <div class="divider-flourish" aria-hidden="true">
        <span>✤</span>
      </div>

      <!-- 6. THE INTERACTIVE INVITATION CARD (UNFOLDING FOLIO) -->
      <div class="interactive-folio-wrapper" id="interactiveFolio">

        <div class="burgundy-folio-envelope">

          <!-- 3D Overlapping Flaps -->
          <div class="envelope-flaps-layer">
            <div class="top-triangle-flap" id="topFlap"></div>
            <div class="left-side-flap"></div>
            <div class="right-side-flap"></div>
          </div>

          <!-- Wax Seal with Monogram -->
          <div class="wax-seal-center-action" id="waxSealButton" onclick="toggleInvitationFolio()" role="button" tabindex="0" aria-label="اضغط لفتح بطاقة الدعوة">
            <div class="wax-seal-button-disc">
              <span class="seal-monogram-text">م & ر</span>
            </div>
            <div class="seal-ribbon-tails">
              <div class="ribbon-blade left"></div>
              <div class="ribbon-blade right"></div>
            </div>
          </div>

          <!-- Prompt Pill -->
          <button type="button" class="unfold-pill-prompt" id="btnPromptUnfold" onclick="toggleInvitationFolio()">
            <span>انقر لفتح البطاقة</span>
            <span style="color:var(--champagne-gold); font-size:15px;">✦</span>
          </button>

          <!-- Inner Letterpress Invitation Card -->
          <article class="inner-unfolded-card" id="innerLetterCard">
            <svg class="inner-card-flora-header" aria-hidden="true">
              <use href="#floral-center-ornament" />
            </svg>

            <p class="inner-card-occasion">عقد قران مبارك</p>

            <p class="inner-card-invitation-text">
              يسعدنا ويشرفنا حضوركم ومشاركتكم فرحتنا الكبرى في هذه الليلة المباركة، متمنين أن يديم الله بيننا المحبة والمسرات في رحاب بيت من بيوت الله.
            </p>

            <div class="divider-flourish" style="margin: 14px auto; max-width: 150px;">
              <span>❦</span>
            </div>

            <!-- BUTTONS: "عرض تفاصيل" MADE SMALLER AS REQUESTED -->
            <div class="inner-card-button-row">
              <a href="#wedding-details" class="btn-details-compact" onclick="smoothScrollTo(event, '#wedding-details')">
                <span>عرض التفاصيل</span>
                <span>↓</span>
              </a>
              <button type="button" class="btn-fold-compact" onclick="toggleInvitationFolio()">
                <span id="labelToggleEnvelope">طي البطاقة</span>
                <span>▲</span>
              </button>
            </div>
          </article>

        </div>

      </div>

    </div>
  </main>

  <!-- ==========================================================
       SECTION 2: WEDDING DETAILS & VENUE
       - Text and frame smaller
       - Timing as full time in single line (not in frames)
       - Paragraph removed
       - Footer photo attribution removed
       - No couple names here
       ========================================================== -->
  <section class="section section-cream" id="wedding-details">
    <div class="container-compact">

      <div class="section-crest">
        <div class="crest-line"></div>
        <span class="crest-symbol">❖</span>
        <div class="crest-line"></div>
      </div>

      <h2 class="section-title">تفاصيل الحفل والمكان</h2>

      <article class="venue-compact-card">

        <!-- Compact Mosque Photo -->
        <div class="venue-photo-compact-frame">
          <img 
            id="venueMosquePhoto"
            class="venue-photo-actual"
            src="assets/al-hosary-mosque.jpg"
            alt="مسجد الحصري - ميدان الحصري، 6 أكتوبر"
            loading="lazy"
            decoding="async"
            onerror="this.onerror=null; this.src='https://upload.wikimedia.org/wikipedia/commons/4/45/Al-Hosary_Mosque_01.jpg';"
          >
          <div class="venue-photo-badge">
            <span>مسجد الحصري</span>
            <span style="color:var(--champagne-gold)">✦</span>
            <span>6 أكتوبر</span>
          </div>
        </div>

        <!-- Official Mosque Strip with 5 Stars -->
        <div class="mosque-metadata-compact-strip">
          <div class="mosque-metadata-text">
            <strong>Al-Hosary Mosque</strong> · ميدان الحصري، First 6th of October, Giza Governorate 12563, Egypt
          </div>
          <div class="mosque-rating-pill" title="تقييم 5 نجوم على خرائط Google">
            <span class="rating-stars-solid">★★★★★</span>
            <span class="rating-label">· Mosque</span>
          </div>
        </div>

        <div class="venue-compact-body">

          <h3 class="venue-compact-title">مسجد الحصري</h3>
          <p class="venue-compact-address">ميدان الحصري، 6 أكتوبر، الجيزة</p>

          <!-- FULL TIME & DATE IN A SINGLE LINE (NOT IN FRAMES) AS REQUESTED -->
          <div class="timing-single-line-container">
            <span class="timing-icon-badge">🗓</span>
            <span>الجمعة، 13 نوفمبر 2026 — الساعة 3:30 مساءً</span>
          </div>

          <!-- Google Maps Button -->
          <a 
            class="btn-maps-solid"
            id="btnGoogleDirections"
            href="https://maps.app.goo.gl/gx99A4hY75tbNW6e8"
            target="_blank"
            rel="noopener noreferrer"
            title="الاتجاهات عبر خرائط Google"
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
              <circle cx="12" cy="10" r="3"></circle>
            </svg>
            <span>الاتجاهات عبر خرائط Google</span>
          </a>

        </div>

      </article>

    </div>
  </section>

  <!-- ==========================================================
       SECTION 3: ARABIC COUNTDOWN
       (No couple names here)
       ========================================================== -->
  <section class="section" id="wedding-countdown">
    <div class="container">

      <div class="section-crest">
        <div class="crest-line"></div>
        <span class="crest-symbol">⌛</span>
        <div class="crest-line"></div>
      </div>

      <h2 class="section-title">الوقت المتبقي حتى نلتقي</h2>
      <p class="section-subtitle">
        نعد الأيام والساعات بشوق ولهفة لمشاركتكم لحظات فرحتنا الكبرى
      </p>

      <!-- Countdown Capsules -->
      <div class="countdown-cluster-row" aria-live="polite">

        <div class="time-capsule-box">
          <span class="capsule-digit-text" id="displayDays">--</span>
          <span class="capsule-unit-label">يوم</span>
        </div>

        <div class="time-capsule-box">
          <span class="capsule-digit-text" id="displayHours">--</span>
          <span class="capsule-unit-label">ساعة</span>
        </div>

        <div class="time-capsule-box">
          <span class="capsule-digit-text" id="displayMinutes">--</span>
          <span class="capsule-unit-label">دقيقة</span>
        </div>

        <div class="time-capsule-box">
          <span class="capsule-digit-text" id="displaySeconds">--</span>
          <span class="capsule-unit-label">ثانية</span>
        </div>

      </div>

      <div class="countdown-live-row" id="countdownStatusBadge">
        <span class="live-pulse-solid"></span>
        <span>العد التنازلي مباشر لموعد عقد القران المبارك</span>
      </div>

    </div>
  </section>

  <!-- ==========================================================
       SECTION 4: IMPORTANT NOTES
       (No couple names here)
       Soft 3D styled icons with website solid colors
       ========================================================== -->
  <section class="section section-cream" id="important-guest-notes">
    <div class="container">

      <div class="section-crest">
        <div class="crest-line"></div>
        <span class="crest-symbol">✦</span>
        <div class="crest-line"></div>
      </div>

      <h2 class="section-title">ملاحظات تهم ضيوفنا</h2>
      <p class="section-subtitle">
        حرصًا منا على راحتكم وتيسير حضوركم في هذا اليوم الاستثنائي
      </p>

      <div class="notes-compact-grid">

        <!-- Parking Note -->
        <article class="note-card-box">
          <div class="note-top-header">
            <div class="note-icon-pod" aria-hidden="true">
              <!-- Solid 3D Styled Car in Website Colors -->
              <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                <ellipse cx="32" cy="50" rx="20" ry="4" fill="#38070e" opacity="0.15"/>
                <path d="M8 38L14 27C16 23 20 21 25 21H39C44 21 48 23 50 27L56 38C58 40 58 44 56 46H8C6 44 6 40 8 38Z" fill="#4a0e17" stroke="#c5a059" stroke-width="1.2"/>
                <path d="M16 28L20 23H44L48 28H16Z" fill="#ffffff" opacity="0.85"/>
                <circle cx="13" cy="38" r="2.5" fill="#d4af37"/>
                <circle cx="51" cy="38" r="2.5" fill="#d4af37"/>
                <circle cx="18" cy="46" r="6" fill="#231417"/>
                <circle cx="18" cy="46" r="3" fill="#c5a059"/>
                <circle cx="46" cy="46" r="6" fill="#231417"/>
                <circle cx="46" cy="46" r="3" fill="#c5a059"/>
              </svg>
            </div>
            <h3 class="note-heading-title">موقف السيارات</h3>
          </div>
          <p class="note-paragraph">
            نظرًا لاحتمالية وجود ازدحام مروري وصعوبة العثور على أماكن لركن السيارات، نرجو من حضراتكم مراعاة ذلك عند تحديد موعد الوصول.
          </p>
        </article>

        <!-- Separate Halls Note -->
        <article class="note-card-box">
          <div class="note-top-header">
            <div class="note-icon-pod" aria-hidden="true">
              <!-- Solid 3D Styled Dual Arches in Website Colors -->
              <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                <ellipse cx="32" cy="52" rx="20" ry="3.5" fill="#38070e" opacity="0.12"/>
                <!-- Men Arch -->
                <path d="M12 48V28C12 21.37 16.48 16 22 16C27.52 16 32 21.37 32 28V48H12Z" fill="#ffffff" stroke="#c5a059" stroke-width="1.2"/>
                <path d="M16 48V29C16 24 18.69 20 22 20C25.31 20 28 24 28 29V48H16Z" fill="#4a0e17"/>
                <!-- Women Arch -->
                <path d="M32 48V28C32 21.37 36.48 16 42 16C47.52 16 52 21.37 52 28V48H32Z" fill="#ffffff" stroke="#c5a059" stroke-width="1.2"/>
                <path d="M36 48V29C36 24 38.69 20 42 20C45.31 20 48 24 48 29V48H36Z" fill="#4a0e17"/>
                <circle cx="32" cy="14" r="2.5" fill="#c5a059"/>
              </svg>
            </div>
            <h3 class="note-heading-title">تنظيم القاعات</h3>
          </div>
          <p class="note-paragraph">
            نود التنويه إلى أن قاعات الرجال والسيدات منفصلة، وذلك لضمان راحة جميع ضيوفنا.
          </p>
        </article>

      </div>

    </div>
  </section>

  <!-- ==========================================================
       SECTION 5: CLOSING SECTION
       Per instruction: Mohamed & Rojain removed from here!
       Solid elegant floral sign-off crest.
       ========================================================== -->
  <section class="closing-section-wrapper" id="closing-farewell">
    <div class="container">
      <div class="closing-content-card">

        <svg style="width:140px; height:28px; margin:0 auto 16px; color:var(--champagne-gold);" aria-hidden="true">
          <use href="#floral-center-ornament" />
        </svg>

        <h2 class="closing-warm-headline">
          بوجودكم تكتمل فرحتنا
        </h2>

        <p class="closing-farewell-text">
          نسعد بحضوركم ومشاركتكم أجمل أيامنا، ونتمنى أن يجمعنا بكم دائمًا الخير والفرح.
        </p>

        <div class="divider-flourish" aria-hidden="true">
          <span>❦</span>
        </div>

        <!-- Solid Elegant Floral Sign-off Emblem (No couple names here) -->
        <div class="closing-floral-emblem" aria-hidden="true">
          <span>✤</span>
          <span>دمتم في خير ومحبة</span>
          <span>✤</span>
        </div>

      </div>
    </div>
  </section>

  <!-- Luxury Editorial Footer -->
  <footer class="editorial-footer-bar">
    <div class="footer-pills-cluster">
      <a 
        class="footer-action-button"
        href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=%D8%B9%D9%82%D8%AF+%D9%82%D8%B1%D8%A7%D9%86+%D9%85%D8%AD%D9%85%D8%AF+%D9%88%D8%B1%D9%88%D8%AC%D9%8A%D9%86&dates=20261113T133000Z/20261113T163000Z&details=%D9%86%D8%AA%D8%B4%D8%B1%D9%81+%D8%A8%D8%AF%D8%B9%D9%88%D8%AA%D9%83%D9%85+%D9%84%D8%AD%D8%B6%D9%88%D8%B1+%D8%B9%D9%82%D8%AF+%D9%82%D8%B1%D8%A7%D9%86+%D9%85%D8%AD%D9%85%D8%AF+%D9%88%D8%B1%D9%88%D8%AC%D9%8A%D9%86+%D8%A8%D9%85%D8%B3%D8%AC%D8%AF+%D8%A7%D9%84%D8%AD%D8%B5%D8%B1%D9%8A&location=%D9%85%D8%B3%D8%AC%D8%AF+%D8%A7%D9%84%D8%AD%D8%B5%D8%B1%D9%8A%D8%8C+%D9%85%D9%8A%D8%AF%D8%A7%D9%86+%D8%A7%D9%84%D8%AD%D8%B5%D8%B1%D9%8A%D8%8C+6+%D8%A3%D9%83%D8%AA%D9%88%D8%A8%D8%B1%D8%8C+%D8%A7%D9%84%D8%AC%D9%8A%D8%B2%D8%A9"
        target="_blank"
        rel="noopener noreferrer"
      >
        <span>📅</span>
        <span>إضافة الموعد إلى تقويم Google</span>
      </a>

      <button type="button" class="footer-action-button" onclick="window.scrollTo({top:0, behavior:'smooth'})">
        <span>▲</span>
        <span>العودة للأعلى</span>
      </button>
    </div>

    <p>دعوة عقد قران مباركة • الجمعة 13 نوفمبر 2026</p>
    <p style="font-size:12px; color:var(--text-light)">بكل المحبة والتقدير ننتظر تشريفكم</p>
  </footer>

  <!-- ==========================================================
       JAVASCRIPT
       ========================================================== -->
  <script>
    /* ----------------------------------------------------
       1. WEDDING DATE & TARGET TIMESTAMP
       Friday, 13 November 2026 - 3:30 PM Cairo Time (UTC+2)
       ---------------------------------------------------- */
    const WEDDING_TARGET_ISO = "2026-11-13T15:30:00+02:00";
    const targetTime = new Date(WEDDING_TARGET_ISO).getTime();

    const arabicNumberFormat = new Intl.NumberFormat("ar-EG", { useGrouping: false });

    function toArabicNumeral(num) {
      if (isNaN(num)) return "٠";
      return arabicNumberFormat.format(num);
    }

    /* ----------------------------------------------------
       2. LIVE COUNTDOWN TIMER
       ---------------------------------------------------- */
    const elDays = document.getElementById("displayDays");
    const elHours = document.getElementById("displayHours");
    const elMinutes = document.getElementById("displayMinutes");
    const elSeconds = document.getElementById("displaySeconds");
    const elStatus = document.getElementById("countdownStatusBadge");

    function runCountdownTick() {
      const now = Date.now();
      const diff = targetTime - now;

      if (diff <= 0) {
        elDays.textContent = "٠";
        elHours.textContent = "٠";
        elMinutes.textContent = "٠";
        elSeconds.textContent = "٠";
        if (elStatus) {
          elStatus.innerHTML = '<span class="live-pulse-solid"></span><span>اليوم هو يوم فرحتنا المبارك، مرحبًا بكم جميعًا!</span>';
        }
        return;
      }

      const totalSeconds = Math.floor(diff / 1000);
      const days = Math.floor(totalSeconds / (3600 * 24));
      const hours = Math.floor((totalSeconds % (3600 * 24)) / 3600);
      const minutes = Math.floor((totalSeconds % 3600) / 60);
      const seconds = totalSeconds % 60;

      elDays.textContent = toArabicNumeral(days);
      elHours.textContent = toArabicNumeral(hours);
      elMinutes.textContent = toArabicNumeral(minutes);
      elSeconds.textContent = toArabicNumeral(seconds);
    }

    runCountdownTick();
    setInterval(runCountdownTick, 1000);

    /* ----------------------------------------------------
       3. INTERACTIVE FOLIO ENVELOPE UNFOLDING
       ---------------------------------------------------- */
    const interactiveFolio = document.getElementById("interactiveFolio");
    const labelToggleEnvelope = document.getElementById("labelToggleEnvelope");
    let isEnvelopeOpen = false;

    function toggleInvitationFolio() {
      isEnvelopeOpen = !isEnvelopeOpen;

      if (isEnvelopeOpen) {
        interactiveFolio.classList.add("is-opened");
        if (labelToggleEnvelope) labelToggleEnvelope.textContent = "طي البطاقة";
      } else {
        interactiveFolio.classList.remove("is-opened");
        if (labelToggleEnvelope) labelToggleEnvelope.textContent = "فتح البطاقة";
      }
    }

    // Keyboard support for wax seal
    const waxSealButton = document.getElementById("waxSealButton");
    if (waxSealButton) {
      waxSealButton.addEventListener("keydown", function(e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          toggleInvitationFolio();
        }
      });
    }

    // Smooth scroll helper
    function smoothScrollTo(event, targetSelector) {
      event.preventDefault();
      const targetElement = document.querySelector(targetSelector);
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: "smooth",
          block: "start"
        });
      }
    }

    /* ----------------------------------------------------
       4. FALLING PETALS CANVAS (SUBTLE BOTANICAL)
       ---------------------------------------------------- */
    const canvas = document.getElementById("petalsCanvas");
    const ctx = canvas.getContext("2d");
    let petals = [];
    const PETAL_COUNT = 16;

    function resizePetalsCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    window.addEventListener("resize", resizePetalsCanvas);
    resizePetalsCanvas();

    class PetalParticle {
      constructor() {
        this.reset(true);
      }

      reset(initial = false) {
        this.x = Math.random() * canvas.width;
        this.y = initial ? Math.random() * canvas.height : -20;
        this.size = Math.random() * 7 + 5;
        this.speedY = Math.random() * 0.7 + 0.3;
        this.speedX = (Math.random() - 0.5) * 0.6;
        this.rotation = Math.random() * 360;
        this.rotationSpeed = (Math.random() - 0.5) * 1.5;
        this.opacity = Math.random() * 0.22 + 0.08;

        const isBurgundy = Math.random() > 0.45;
        this.color = isBurgundy
          ? `rgba(142, 43, 60, ${this.opacity})`
          : `rgba(197, 160, 89, ${this.opacity})`;
      }

      update() {
        this.y += this.speedY;
        this.x += Math.sin(this.y * 0.008) * 0.6;
        this.rotation += this.rotationSpeed;

        if (this.y > canvas.height + 20 || this.x < -20 || this.x > canvas.width + 20) {
          this.reset(false);
        }
      }

      draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate((this.rotation * Math.PI) / 180);
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.ellipse(0, 0, this.size * 0.5, this.size, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }
    }

    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!prefersReducedMotion) {
      for (let i = 0; i < PETAL_COUNT; i++) {
        petals.push(new PetalParticle());
      }

      function loopPetals() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        petals.forEach((p) => {
          p.update();
          p.draw();
        });
        requestAnimationFrame(loopPetals);
      }
      loopPetals();
    }

    /* ----------------------------------------------------
       5. AMBIENT HARP SYNTHESIZER (WEB AUDIO API)
       Pure serenity - zero external asset!
       Muted by default.
       ---------------------------------------------------- */
    const btnAudio = document.getElementById("btnAmbientAudio");
    const audioSymbol = document.getElementById("audioSymbol");
    const audioLabelText = document.getElementById("audioLabelText");
    let audioContext = null;
    let isMelodyPlaying = false;
    let melodyTimer = null;

    const harpNotes = [293.66, 329.63, 349.23, 392.00, 440.00, 466.16, 523.25, 587.33];

    function playSereneNote(frequency, duration = 2.6) {
      if (!audioContext) return;
      const osc = audioContext.createOscillator();
      const gain = audioContext.createGain();

      osc.type = "sine";
      osc.frequency.setValueAtTime(frequency, audioContext.currentTime);

      gain.gain.setValueAtTime(0.0001, audioContext.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.03, audioContext.currentTime + 0.1);
      gain.gain.exponentialRampToValueAtTime(0.0001, audioContext.currentTime + duration);

      osc.connect(gain);
      gain.connect(audioContext.destination);

      osc.start();
      osc.stop(audioContext.currentTime + duration);
    }

    function startMusic() {
      if (!audioContext) {
        audioContext = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioContext.state === "suspended") {
        audioContext.resume();
      }

      isMelodyPlaying = true;
      btnAudio.classList.add("active");
      audioSymbol.textContent = "⏸";
      audioLabelText.textContent = "إيقاف النغمات";

      let beat = 0;
      melodyTimer = setInterval(() => {
        if (!isMelodyPlaying) return;
        const noteIdx = Math.floor(Math.random() * harpNotes.length);
        playSereneNote(harpNotes[noteIdx], 3.0);

        if (beat % 2 === 0) {
          setTimeout(() => {
            if (isMelodyPlaying) {
              const chordIdx = (noteIdx + 4) % harpNotes.length;
              playSereneNote(harpNotes[chordIdx] * 0.5, 3.8);
            }
          }, 400);
        }
        beat++;
      }, 1700);
    }

    function stopMusic() {
      isMelodyPlaying = false;
      btnAudio.classList.remove("active");
      audioSymbol.textContent = "♪";
      audioLabelText.textContent = "نغمات هادئة";
      if (melodyTimer) {
        clearInterval(melodyTimer);
        melodyTimer = null;
      }
    }

    btnAudio.addEventListener("click", () => {
      if (!isMelodyPlaying) {
        startMusic();
      } else {
        stopMusic();
      }
    });

    /* ----------------------------------------------------
       6. SHARE VIA WHATSAPP / WEB SHARE API
       ---------------------------------------------------- */
    const btnShare = document.getElementById("btnShareWhatsApp");
    btnShare.addEventListener("click", () => {
      const shareContent = {
        title: "دعوة عقد قران محمد & روجين",
        text: "نتشرف بدعوتكم لحضور حفل عقد قران محمد & روجين بمسجد الحصري - 6 أكتوبر، يوم الجمعة 13 نوفمبر 2026 الساعة 3:30 مساءً.",
        url: window.location.href
      };

      if (navigator.share) {
        navigator.share(shareContent).catch(() => {});
      } else {
        const shareMessage = "نتشرف بدعوتكم لحضور حفل عقد قران محمد & روجين بمسجد الحصري، الجمعة 13 نوفمبر 2026 - " + window.location.href;
        const url = "https://api.whatsapp.com/send?text=" + encodeURIComponent(shareMessage);
        window.open(url, "_blank");
      }
    });
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('message.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully generated updated index.html and message.html!")

