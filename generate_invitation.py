# -*- coding: utf-8 -*-
"""
Generator for the Elegant Arabic Wedding Invitation Website
Mohamed & Rodgin (محمد & روجين)
"""

html_code = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#4a0e17">
  <title>دعوة عقد قران | محمد & روجين</title>

  <!-- Google Fonts: Aref Ruqaa for majestic royal calligraphy, Amiri for Quranic verses, Alexandria for refined editorial body -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Alexandria:wght@300;400;500;600;700&family=Amiri:ital,wght@0,400;0,700;1,400&family=Aref+Ruqaa:wght@400;700&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================
       DESIGN SYSTEM & COLOR PALETTE
       Suited to the reference image:
       - Deep Royal Burgundy: #4a0e17, #58141f, #38070e, #6e1d2a
       - Embossed Velvet Wine: #8e2b3c, #7a2230
       - Warm Editorial Ivory: #faf7f2, #fdfcf9, #f4ede1
       - Champagne Gold & Muted Metallic Foil: #c5a059, #e4c57c, #8a6829
       - Warm Typography: #231417, #453034, #6e575c
       ========================================================== */
    :root {
      --burgundy-deep: #38070e;
      --burgundy-main: #4a0e17;
      --burgundy-rich: #58141f;
      --burgundy-wine: #6e1d2a;
      --burgundy-light: #8e2b3c;
      --burgundy-tint: rgba(74, 14, 23, 0.05);

      --ivory-base: #faf7f2;
      --ivory-paper: #fdfcf9;
      --ivory-card: #f8f4ec;
      --champagne-tint: #f3ebdc;
      --champagne-gold: #c5a059;
      --champagne-bright: #e4c57c;
      --gold-deep: #7d5e2a;

      --gold-gradient: linear-gradient(135deg, #b88d4c 0%, #e8ca88 45%, #c5a059 70%, #8f692b 100%);
      --burgundy-gradient: linear-gradient(145deg, #601521 0%, #4a0e17 50%, #35080f 100%);
      --velvet-gradient: radial-gradient(circle at 40% 30%, #6e1d2a 0%, #4a0e17 60%, #30060c 100%);

      --text-main: #231417;
      --text-editorial: #453034;
      --text-muted: #6e575c;
      --text-light: #947e83;

      --border-subtle: rgba(197, 160, 89, 0.28);
      --border-medium: rgba(197, 160, 89, 0.45);
      --border-burgundy-subtle: rgba(74, 14, 23, 0.15);

      --shadow-soft: 0 10px 30px rgba(58, 10, 17, 0.05);
      --shadow-card: 0 16px 45px rgba(58, 10, 17, 0.08);
      --shadow-deep: 0 25px 70px rgba(58, 10, 17, 0.14);

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

    body {
      font-family: var(--font-body);
      background-color: var(--ivory-base);
      background-image: 
        radial-gradient(ellipse at 50% 0%, rgba(243, 235, 220, 0.65) 0%, rgba(250, 247, 242, 0.95) 75%),
        url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23c5a059' fill-opacity='0.035' fill-rule='evenodd'%3E%3Cpath d='M30 30L15 15l15-15 15 15-15 15zm0 0l15 15-15 15-15-15 15-15z'/%3E%3C/g%3E%3C/svg%3E");
      line-height: 1.9;
      font-size: 16px;
      overflow-x: hidden;
      position: relative;
    }

    ::selection {
      background: rgba(110, 29, 42, 0.18);
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
      width: min(100% - 36px, 860px);
      margin-inline: auto;
      position: relative;
      z-index: 2;
    }

    .container-narrow {
      width: min(100% - 36px, 680px);
      margin-inline: auto;
      position: relative;
      z-index: 2;
    }

    /* Luxury Hairline Gold & Burgundy Framing */
    .luxury-frame-bar {
      position: fixed;
      left: 0;
      right: 0;
      height: 4px;
      z-index: 999;
      pointer-events: none;
      background: linear-gradient(90deg, 
        transparent 0%, 
        var(--burgundy-main) 20%, 
        var(--champagne-bright) 50%, 
        var(--burgundy-main) 80%, 
        transparent 100%
      );
    }
    .frame-bar-top { top: 0; }
    .frame-bar-bottom { bottom: 0; }

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
      background: rgba(253, 252, 249, 0.92);
      backdrop-filter: blur(10px);
      border: 1px solid var(--border-medium);
      border-radius: 30px;
      padding: 7px 15px;
      font-size: 13px;
      color: var(--burgundy-main);
      display: inline-flex;
      align-items: center;
      gap: 7px;
      box-shadow: 0 4px 15px rgba(74, 14, 23, 0.08);
      transition: all 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
      cursor: pointer;
    }

    .pill-btn:hover {
      background: #ffffff;
      border-color: var(--champagne-gold);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(74, 14, 23, 0.15);
      color: var(--burgundy-wine);
    }

    .pill-btn.active {
      background: var(--burgundy-main);
      color: #fff;
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
      padding: 100px 18px;
      text-align: center;
    }

    .section-editorial {
      background: transparent;
    }

    .section-cream {
      background: linear-gradient(180deg, rgba(248, 244, 236, 0.5) 0%, rgba(243, 235, 220, 0.7) 50%, rgba(248, 244, 236, 0.5) 100%);
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
    }

    /* Section Headers */
    .section-crest {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      margin-bottom: 16px;
      color: var(--champagne-gold);
    }

    .crest-line {
      width: 45px;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--champagne-gold));
    }

    .crest-line.left {
      background: linear-gradient(90deg, var(--champagne-gold), transparent);
    }

    .crest-symbol {
      font-size: 16px;
      color: var(--champagne-gold);
      letter-spacing: 2px;
    }

    .section-title {
      font-family: var(--font-names);
      font-size: clamp(30px, 6vw, 44px);
      font-weight: 400;
      color: var(--burgundy-deep);
      margin-bottom: 10px;
      letter-spacing: -0.5px;
    }

    .section-subtitle {
      font-size: clamp(14.5px, 3vw, 16.5px);
      color: var(--text-muted);
      max-width: 520px;
      margin: 0 auto 40px;
      line-height: 1.85;
      font-weight: 400;
    }

    /* Flourish & Dividers */
    .divider-flourish {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      margin: 28px auto;
      max-width: 240px;
      color: var(--champagne-gold);
      opacity: 0.9;
    }

    .divider-flourish::before,
    .divider-flourish::after {
      content: "";
      flex: 1;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--champagne-gold), transparent);
    }

    /* ==========================================================
       SECTION 1: OPENING SECTION
       Arranged strictly vertically.
       First & most visually prominent element: The Names!
       ========================================================== */
    .opening-section {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 85px 18px 90px;
      position: relative;
      text-align: center;
      background: 
        radial-gradient(ellipse at 50% 25%, #ffffff 0%, rgba(253, 251, 247, 0.92) 50%, rgba(246, 239, 229, 0.65) 100%);
    }

    .editorial-hero-card {
      max-width: 760px;
      width: 100%;
      margin: 0 auto;
      padding: 60px 38px 55px;
      background: rgba(255, 255, 255, 0.88);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      box-shadow: 
        0 25px 65px rgba(74, 14, 23, 0.07),
        inset 0 0 0 6px #ffffff,
        inset 0 0 0 7.5px var(--border-subtle);
      position: relative;
      overflow: hidden;
    }

    /* Corner Watermark Accents from the burgundy envelope texture */
    .corner-floral-watermark {
      position: absolute;
      width: 120px;
      height: 120px;
      opacity: 0.08;
      pointer-events: none;
      background-image: url('assets/burgundy-envelope-ref.jpg');
      background-size: cover;
      filter: contrast(1.4);
      border-radius: 50%;
    }
    .watermark-top-right { top: -20px; right: -20px; }
    .watermark-bottom-left { bottom: -20px; left: -20px; }

    /* Corner filigree */
    .filigree-corner {
      position: absolute;
      width: 32px;
      height: 32px;
      color: var(--champagne-gold);
      pointer-events: none;
      opacity: 0.85;
    }
    .filigree-tr { top: 12px; right: 12px; }
    .filigree-tl { top: 12px; left: 12px; transform: scaleX(-1); }
    .filigree-br { bottom: 12px; right: 12px; transform: scaleY(-1); }
    .filigree-bl { bottom: 12px; left: 12px; transform: scale(-1); }

    /* Monogram Crest at top */
    .monogram-crest-top {
      margin-bottom: 24px;
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
    }

    .monogram-seal-disc {
      width: 66px;
      height: 66px;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, #7a2230 0%, #4a0e17 60%, #30060c 100%);
      border: 1.5px solid var(--champagne-bright);
      box-shadow: 
        0 6px 18px rgba(74, 14, 23, 0.28),
        inset 0 2px 4px rgba(255, 255, 255, 0.35);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--champagne-bright);
      font-family: var(--font-names);
      font-size: 24px;
      letter-spacing: 1px;
    }

    /* ----------------------------------------------------
       THE NAMES: FIRST AND MOST VISUALLY PROMINENT ELEMENT
       ---------------------------------------------------- */
    .grand-couple-hero {
      margin-bottom: 25px;
    }

    .grand-couple-names {
      font-family: var(--font-names);
      font-size: clamp(52px, 11vw, 88px);
      line-height: 1.25;
      margin: 0;
      color: var(--burgundy-deep);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 20px;
      flex-wrap: wrap;
    }

    .grand-couple-names .name-groom,
    .grand-couple-names .name-bride {
      display: inline-block;
      background: linear-gradient(145deg, #4a0e17 0%, #6e1d2a 40%, #8e2b3c 60%, #38070e 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 3px 10px rgba(74, 14, 23, 0.16));
      transition: transform 0.4s ease;
      position: relative;
    }

    .grand-couple-names .name-groom:hover,
    .grand-couple-names .name-bride:hover {
      transform: scale(1.02);
    }

    .grand-couple-names .couple-connector {
      font-family: var(--font-names);
      font-size: clamp(34px, 7vw, 54px);
      color: var(--champagne-gold);
      -webkit-text-fill-color: var(--champagne-gold);
      opacity: 0.95;
      font-weight: 400;
      transform: translateY(-2px);
    }

    .hero-names-subbar {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      margin-top: 6px;
      color: var(--champagne-gold);
      font-size: 13.5px;
      letter-spacing: 2px;
    }

    /* Vertically Stacked Content Elements */
    .bismillah-calligraphy {
      font-family: var(--font-calligraphy);
      font-size: clamp(22px, 4.5vw, 29px);
      color: var(--burgundy-rich);
      margin: 24px 0 20px;
      letter-spacing: 0.5px;
      font-weight: 700;
    }

    .invitation-formal-phrase {
      font-size: clamp(17px, 3.4vw, 20px);
      color: var(--text-editorial);
      line-height: 2.1;
      margin-bottom: 14px;
      font-weight: 500;
    }

    .lineage-card {
      margin: 18px auto 24px;
      padding: 16px 24px;
      max-width: 580px;
      background: rgba(248, 244, 236, 0.7);
      border-top: 1px solid var(--border-medium);
      border-bottom: 1px solid var(--border-medium);
      border-radius: 4px;
    }

    .lineage-text {
      font-size: clamp(17px, 3.4vw, 21px);
      color: var(--burgundy-deep);
      line-height: 2;
    }

    .lineage-text .highlight-groom,
    .lineage-text .highlight-bride {
      font-family: var(--font-names);
      font-size: clamp(26px, 5.2vw, 34px);
      color: var(--burgundy-main);
      font-weight: 700;
      display: inline-block;
      margin-inline: 4px;
    }

    .heartfelt-invitation-message {
      font-size: clamp(16px, 3.2vw, 19px);
      color: var(--text-muted);
      line-height: 2.2;
      max-width: 580px;
      margin: 18px auto 24px;
      font-weight: 400;
    }

    .prophetic-dua-capsule {
      display: inline-block;
      padding: 14px 28px;
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(248, 244, 236, 0.9));
      border: 1px solid var(--champagne-gold);
      border-radius: 40px;
      box-shadow: 0 6px 20px rgba(74, 14, 23, 0.08);
      margin-top: 6px;
    }

    .prophetic-dua-text {
      font-family: var(--font-calligraphy);
      font-size: clamp(18px, 3.6vw, 22px);
      color: var(--burgundy-rich);
      font-weight: 700;
      letter-spacing: 0.3px;
    }

    /* Scroll Prompt */
    .open-card-scroll-prompt {
      margin-top: 45px;
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
      color: var(--burgundy-main);
      font-size: 14px;
      font-weight: 500;
      transition: all 0.35s ease;
      cursor: pointer;
    }

    .open-card-scroll-prompt:hover {
      color: var(--burgundy-light);
      transform: translateY(3px);
    }

    .mouse-scroll-indicator {
      width: 24px;
      height: 38px;
      border: 1.5px solid var(--champagne-gold);
      border-radius: 14px;
      position: relative;
      background: rgba(255, 255, 255, 0.6);
    }

    .mouse-wheel-dot {
      width: 4px;
      height: 7px;
      background: var(--burgundy-main);
      border-radius: 2px;
      position: absolute;
      top: 6px;
      left: 50%;
      transform: translateX(-50%);
      animation: mouseWheel 2.2s infinite ease-in-out;
    }

    @keyframes mouseWheel {
      0%, 100% { transform: translate(-50%, 0); opacity: 1; }
      50% { transform: translate(-50%, 11px); opacity: 0.2; }
    }

    /* ==========================================================
       SECTION 2: INTERACTIVE INVITATION CARD (UNFOLDING CEREMONY)
       Bespoke envelope in Burgundy embossed floral texture matching
       the reference photo with overlapping flaps and 3D wax seal.
       ========================================================== */
    .interactive-section {
      padding: 105px 18px;
      background: linear-gradient(180deg, #faf7f2 0%, #f3ebdc 50%, #faf7f2 100%);
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
    }

    .envelope-theater {
      max-width: 620px;
      margin: 0 auto;
      perspective: 1600px;
      position: relative;
    }

    /* Outer Folio / Envelope Jacket */
    .burgundy-envelope {
      width: 100%;
      position: relative;
      border-radius: 8px;
      box-shadow: 
        0 25px 70px rgba(58, 10, 17, 0.22),
        0 8px 25px rgba(58, 10, 17, 0.12);
      transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
      overflow: visible;
      background-color: var(--burgundy-rich);
      background-image: 
        linear-gradient(rgba(74, 14, 23, 0.65), rgba(56, 7, 14, 0.82)),
        url('assets/burgundy-envelope-ref.jpg');
      background-size: cover;
      background-position: center;
      border: 1px solid rgba(228, 197, 124, 0.35);
      min-height: 480px;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
    }

    /* 3D Diagonal Envelope Flaps matching reference image */
    .flap-container {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 15;
    }

    /* Top Triangular Flap */
    .flap-top {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 250px;
      transform-origin: top center;
      transform-style: preserve-3d;
      transition: transform 1.2s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 25;
      background-image: 
        linear-gradient(145deg, rgba(96, 21, 33, 0.75), rgba(58, 10, 17, 0.92)),
        url('assets/burgundy-envelope-ref.jpg');
      background-size: cover;
      background-position: top center;
      clip-path: polygon(0 0, 100% 0, 50% 100%);
      filter: drop-shadow(0 12px 25px rgba(35, 4, 8, 0.4));
      border-bottom: 1.5px solid rgba(228, 197, 124, 0.45);
    }

    .flap-top::after {
      content: "";
      position: absolute;
      inset: 6px;
      clip-path: polygon(0 0, 100% 0, 50% 100%);
      border-bottom: 1px dashed rgba(228, 197, 124, 0.35);
    }

    /* Left and Right Overlapping Triangular Flaps */
    .flap-left-angle {
      position: absolute;
      top: 0;
      left: 0;
      bottom: 0;
      width: 55%;
      clip-path: polygon(0 0, 100% 50%, 0 100%);
      background-image: 
        linear-gradient(135deg, rgba(88, 20, 31, 0.8), rgba(58, 10, 17, 0.95)),
        url('assets/burgundy-envelope-ref.jpg');
      background-size: cover;
      background-position: left center;
      z-index: 18;
      border-right: 1px solid rgba(228, 197, 124, 0.25);
      filter: drop-shadow(4px 0 12px rgba(25, 3, 6, 0.35));
      transition: transform 0.9s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .flap-right-angle {
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      width: 55%;
      clip-path: polygon(100% 0, 0 50%, 100% 100%);
      background-image: 
        linear-gradient(225deg, rgba(88, 20, 31, 0.8), rgba(58, 10, 17, 0.95)),
        url('assets/burgundy-envelope-ref.jpg');
      background-size: cover;
      background-position: right center;
      z-index: 19;
      border-left: 1px solid rgba(228, 197, 124, 0.25);
      filter: drop-shadow(-4px 0 12px rgba(25, 3, 6, 0.35));
      transition: transform 0.9s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* Central Wax Seal with Monogram */
    .wax-seal-center-stage {
      position: absolute;
      top: 215px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 35;
      cursor: pointer;
      transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    .wax-seal-center-stage:hover {
      transform: translateX(-50%) scale(1.08);
    }

    .wax-seal-disc {
      width: 82px;
      height: 82px;
      border-radius: 50%;
      background: radial-gradient(circle at 35% 35%, #912b3b 0%, #631723 40%, #4a0e17 80%, #30060c 100%);
      box-shadow: 
        0 10px 25px rgba(35, 4, 8, 0.6),
        inset 0 3px 6px rgba(255, 255, 255, 0.35),
        inset 0 -3px 6px rgba(0, 0, 0, 0.5);
      border: 2px solid #deb97a;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #fcf6ea;
      text-shadow: 0 1px 3px rgba(30, 4, 8, 0.8);
      position: relative;
    }

    .wax-seal-disc::before {
      content: "";
      position: absolute;
      inset: 4px;
      border-radius: 50%;
      border: 1px dashed rgba(255, 246, 225, 0.4);
      pointer-events: none;
    }

    .seal-monogram-initials {
      font-family: var(--font-names);
      font-size: 28px;
      font-weight: 700;
      line-height: 1;
      letter-spacing: 1px;
    }

    /* Silk Ribbon hanging beneath seal */
    .seal-silk-ribbons {
      position: absolute;
      bottom: -22px;
      left: 50%;
      transform: translateX(-50%);
      width: 50px;
      height: 28px;
      display: flex;
      justify-content: center;
      gap: 6px;
      z-index: -1;
    }

    .silk-tail {
      width: 16px;
      height: 30px;
      background: linear-gradient(180deg, #c5a059 0%, #8a6829 100%);
      clip-path: polygon(0 0, 100% 0, 100% 80%, 50% 100%, 0 80%);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.25);
    }
    .silk-tail.left { transform: rotate(16deg); }
    .silk-tail.right { transform: rotate(-16deg); }

    /* Interactive Invite Prompt Button */
    .unfold-action-prompt {
      position: absolute;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(253, 252, 249, 0.95);
      backdrop-filter: blur(8px);
      border: 1px solid var(--champagne-gold);
      color: var(--burgundy-deep);
      padding: 10px 24px;
      border-radius: 30px;
      font-size: 14.5px;
      font-weight: 600;
      white-space: nowrap;
      box-shadow: 0 8px 25px rgba(45, 6, 12, 0.25);
      display: inline-flex;
      align-items: center;
      gap: 9px;
      cursor: pointer;
      transition: all 0.35s ease;
      z-index: 30;
      animation: sealPulse 2.6s infinite ease-in-out;
    }

    @keyframes sealPulse {
      0%, 100% { box-shadow: 0 8px 22px rgba(45, 6, 12, 0.25); transform: translateX(-50%) translateY(0); }
      50% { box-shadow: 0 12px 32px rgba(197, 160, 89, 0.45); transform: translateX(-50%) translateY(-3px); }
    }

    .unfold-action-prompt:hover {
      background: #ffffff;
      border-color: var(--burgundy-main);
      color: var(--burgundy-main);
    }

    /* Inner Letterpress Card */
    .inner-letterpress-card {
      background: var(--ivory-paper);
      background-image: 
        radial-gradient(ellipse at 50% 30%, #ffffff 0%, rgba(253, 252, 249, 0.95) 70%, rgba(247, 241, 231, 0.7) 100%);
      padding: 60px 40px 50px;
      border-radius: 6px;
      text-align: center;
      position: relative;
      z-index: 10;
      border: 1px solid var(--border-medium);
      box-shadow: 
        inset 0 0 0 8px #ffffff,
        inset 0 0 0 9.5px var(--border-subtle);
      transition: all 1s cubic-bezier(0.16, 1, 0.3, 1);
      opacity: 0.95;
    }

    .card-golden-header {
      width: 140px;
      height: 34px;
      margin: 0 auto 15px;
      color: var(--champagne-gold);
    }

    .card-occasion-title {
      font-family: var(--font-calligraphy);
      font-size: 20px;
      color: var(--champagne-gold);
      font-weight: 700;
      letter-spacing: 1px;
      margin-bottom: 8px;
    }

    .card-grand-names {
      font-family: var(--font-names);
      font-size: clamp(36px, 7.5vw, 52px);
      color: var(--burgundy-main);
      line-height: 1.3;
      margin: 10px 0 18px;
    }

    .card-warm-message {
      color: var(--text-editorial);
      font-size: clamp(15.5px, 3.2vw, 17.5px);
      line-height: 2.1;
      max-width: 480px;
      margin: 0 auto 20px;
    }

    .card-cta-group {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      justify-content: center;
      margin-top: 28px;
    }

    .btn-card-primary {
      background: var(--burgundy-gradient);
      color: #ffffff;
      padding: 12px 28px;
      border-radius: 4px;
      font-size: 15px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 6px 18px rgba(74, 14, 23, 0.25);
      transition: all 0.35s ease;
      border: 1px solid rgba(228, 197, 124, 0.3);
    }

    .btn-card-primary:hover {
      background: linear-gradient(145deg, #741a27 0%, #58141f 50%, #400a12 100%);
      transform: translateY(-2px);
      box-shadow: 0 10px 25px rgba(74, 14, 23, 0.35);
      color: #fff;
    }

    .btn-card-outline {
      background: transparent;
      color: var(--burgundy-main);
      padding: 12px 24px;
      border-radius: 4px;
      font-size: 15px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border: 1px solid var(--border-medium);
      transition: all 0.35s ease;
    }

    .btn-card-outline:hover {
      background: rgba(74, 14, 23, 0.06);
      border-color: var(--burgundy-main);
      transform: translateY(-2px);
    }

    /* OPENED STATE */
    .envelope-theater.is-opened .flap-top {
      transform: rotateX(175deg);
      z-index: 5;
    }

    .envelope-theater.is-opened .flap-left-angle {
      transform: translateX(-40px) rotateY(-25deg);
      opacity: 0.15;
    }

    .envelope-theater.is-opened .flap-right-angle {
      transform: translateX(40px) rotateY(25deg);
      opacity: 0.15;
    }

    .envelope-theater.is-opened .wax-seal-center-stage {
      transform: translateX(-50%) translateY(-65px) scale(0.8);
      opacity: 0.2;
      pointer-events: none;
    }

    .envelope-theater.is-opened .unfold-action-prompt {
      opacity: 0;
      pointer-events: none;
      visibility: hidden;
    }

    .envelope-theater.is-opened .inner-letterpress-card {
      transform: translateY(-12px);
      box-shadow: 
        0 25px 60px rgba(58, 10, 17, 0.18),
        inset 0 0 0 8px #ffffff,
        inset 0 0 0 9.5px var(--border-subtle);
      opacity: 1;
    }

    /* ==========================================================
       SECTION 3: WEDDING DETAILS & VENUE
       ========================================================== */
    .venue-grand-card {
      max-width: 760px;
      margin: 0 auto;
      background: var(--ivory-paper);
      border-radius: 8px;
      border: 1px solid var(--border-medium);
      box-shadow: var(--shadow-deep);
      overflow: hidden;
      position: relative;
    }

    .venue-photograph-frame {
      position: relative;
      width: 100%;
      height: 380px;
      overflow: hidden;
      background-color: #2b1216;
    }

    .venue-actual-photo {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 38%;
      display: block;
      transition: transform 0.9s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    .venue-grand-card:hover .venue-actual-photo {
      transform: scale(1.035);
    }

    .venue-photo-gradient-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(40, 10, 15, 0.1) 0%, rgba(40, 10, 15, 0.7) 100%);
      pointer-events: none;
    }

    .venue-photo-tag {
      position: absolute;
      bottom: 20px;
      right: 24px;
      background: rgba(253, 252, 249, 0.94);
      backdrop-filter: blur(8px);
      padding: 7px 18px;
      border-radius: 30px;
      font-size: 14px;
      font-weight: 600;
      color: var(--burgundy-deep);
      border: 1px solid var(--border-subtle);
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.2);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Metadata Banner */
    .mosque-metadata-banner {
      background: linear-gradient(135deg, rgba(74, 14, 23, 0.04), rgba(197, 160, 89, 0.08));
      border-bottom: 1px solid var(--border-subtle);
      padding: 16px 24px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      text-align: right;
    }

    .mosque-official-meta {
      font-size: 13.5px;
      color: var(--text-editorial);
      line-height: 1.6;
    }

    .mosque-rating-cluster {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #ffffff;
      padding: 5px 14px;
      border-radius: 20px;
      border: 1px solid var(--border-subtle);
      box-shadow: 0 2px 8px rgba(74, 14, 23, 0.04);
    }

    .rating-stars-3d {
      color: #e5b338;
      font-size: 15px;
      letter-spacing: 2px;
      text-shadow: 0 1px 3px rgba(197, 160, 89, 0.4);
    }

    .rating-category-pill {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--burgundy-main);
    }

    /* Main Venue Details Body */
    .venue-card-body {
      padding: 38px 32px 42px;
      text-align: center;
    }

    .venue-headline-name {
      font-family: var(--font-names);
      font-size: clamp(32px, 6.5vw, 46px);
      color: var(--burgundy-deep);
      margin-bottom: 8px;
      font-weight: 400;
    }

    .venue-detailed-address {
      color: var(--text-muted);
      font-size: 17px;
      line-height: 1.8;
      margin-bottom: 30px;
    }

    /* 2x2 Grid with SOFT 3D ICONS in website colors */
    .event-spec-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 18px;
      margin: 28px auto;
      max-width: 620px;
      text-align: right;
    }

    .spec-capsule {
      background: rgba(250, 246, 240, 0.65);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 20px 18px;
      display: flex;
      align-items: center;
      gap: 16px;
      transition: all 0.35s ease;
      position: relative;
    }

    .spec-capsule:hover {
      background: #ffffff;
      border-color: var(--champagne-gold);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(74, 14, 23, 0.06);
    }

    /* Soft 3D Icon Container */
    .soft-3d-icon-box {
      width: 54px;
      height: 54px;
      border-radius: 12px;
      background: linear-gradient(135deg, #ffffff 0%, #f4ede1 100%);
      border: 1px solid var(--border-medium);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 
        0 6px 16px rgba(74, 14, 23, 0.08),
        inset 0 1px 2px rgba(255, 255, 255, 0.9);
      position: relative;
    }

    .soft-3d-icon-box svg {
      width: 34px;
      height: 34px;
      filter: drop-shadow(0 2px 4px rgba(74, 14, 23, 0.15));
    }

    .spec-details {
      flex: 1;
    }

    .spec-label {
      font-size: 13px;
      color: var(--text-light);
      margin-bottom: 3px;
      font-weight: 500;
    }

    .spec-val {
      font-size: 16.5px;
      font-weight: 700;
      color: var(--burgundy-deep);
      line-height: 1.4;
    }

    /* Google Maps Directions Action */
    .maps-action-zone {
      margin-top: 34px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 14px;
    }

    .btn-google-directions {
      background: var(--burgundy-gradient);
      color: #ffffff;
      padding: 15px 36px;
      border-radius: 4px;
      font-size: 16.5px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 12px;
      box-shadow: 0 8px 25px rgba(74, 14, 23, 0.32);
      transition: all 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
      letter-spacing: 0.3px;
      border: 1px solid rgba(228, 197, 124, 0.3);
    }

    .btn-google-directions:hover {
      background: linear-gradient(145deg, #741a27 0%, #58141f 50%, #3e0a12 100%);
      transform: translateY(-3px);
      box-shadow: 0 14px 35px rgba(74, 14, 23, 0.42);
      color: #ffffff;
    }

    .btn-google-directions svg {
      width: 22px;
      height: 22px;
      color: var(--champagne-bright);
    }

    .photo-credit-footnote {
      font-size: 11.5px;
      color: var(--text-light);
    }

    /* ==========================================================
       SECTION 4: ARABIC COUNTDOWN
       ========================================================== */
    .countdown-section {
      background: radial-gradient(circle at 50% 50%, #ffffff 0%, #faf6ef 60%, #f4ede1 100%);
      padding: 100px 18px;
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
    }

    .countdown-capsule-row {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
      margin: 35px auto 25px;
      max-width: 680px;
      direction: rtl;
    }

    .time-capsule {
      flex: 1 1 125px;
      max-width: 145px;
      min-width: 110px;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      padding: 22px 10px 18px;
      text-align: center;
      box-shadow: 
        0 10px 25px rgba(74, 14, 23, 0.05),
        inset 0 0 0 3px #ffffff,
        inset 0 0 0 4.5px var(--border-subtle);
      position: relative;
      transition: all 0.35s ease;
    }

    .time-capsule:hover {
      transform: translateY(-4px);
      border-color: var(--champagne-gold);
      box-shadow: 0 16px 35px rgba(74, 14, 23, 0.12);
      background: #ffffff;
    }

    .capsule-number {
      font-family: var(--font-names);
      font-size: clamp(38px, 8vw, 56px);
      font-weight: 700;
      color: var(--burgundy-deep);
      line-height: 1.1;
      display: block;
      margin-bottom: 5px;
      text-shadow: 0 1px 3px rgba(74, 14, 23, 0.12);
    }

    .capsule-unit {
      font-size: 14.5px;
      color: var(--text-muted);
      font-weight: 600;
      display: block;
    }

    .countdown-live-badge {
      font-size: 14.5px;
      color: var(--burgundy-main);
      margin-top: 26px;
      font-weight: 500;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 9px;
    }

    .live-pulse-dot {
      width: 9px;
      height: 9px;
      background: var(--burgundy-light);
      border-radius: 50%;
      box-shadow: 0 0 0 rgba(142, 43, 60, 0.4);
      animation: livePulse 2s infinite;
    }

    @keyframes livePulse {
      0% { box-shadow: 0 0 0 0 rgba(142, 43, 60, 0.7); }
      70% { box-shadow: 0 0 0 10px rgba(142, 43, 60, 0); }
      100% { box-shadow: 0 0 0 0 rgba(142, 43, 60, 0); }
    }

    /* ==========================================================
       SECTION 5: IMPORTANT NOTES
       ========================================================== */
    .notes-section {
      background: linear-gradient(180deg, #faf7f2 0%, #f4ede1 50%, #faf7f2 100%);
      padding: 100px 18px;
    }

    .notes-luxury-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
      max-width: 760px;
      margin: 0 auto;
    }

    .note-card-3d {
      background: rgba(255, 255, 255, 0.88);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      padding: 34px 28px;
      text-align: right;
      position: relative;
      box-shadow: var(--shadow-card);
      transition: all 0.35s ease;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .note-card-3d:hover {
      background: #ffffff;
      transform: translateY(-3px);
      border-color: var(--champagne-gold);
      box-shadow: var(--shadow-deep);
    }

    .note-header-3d {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .note-3d-icon {
      width: 58px;
      height: 58px;
      border-radius: 14px;
      background: linear-gradient(135deg, #ffffff 0%, #f3ebdc 100%);
      border: 1px solid var(--border-medium);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 
        0 6px 18px rgba(74, 14, 23, 0.08),
        inset 0 1px 3px rgba(255, 255, 255, 0.9);
    }

    .note-3d-icon svg {
      width: 38px;
      height: 38px;
      filter: drop-shadow(0 2px 5px rgba(74, 14, 23, 0.16));
    }

    .note-title-3d {
      font-family: var(--font-names);
      font-size: 23px;
      color: var(--burgundy-deep);
      font-weight: 400;
    }

    .note-content-p {
      color: var(--text-editorial);
      font-size: 15.5px;
      line-height: 2.1;
      font-weight: 400;
    }

    /* ==========================================================
       SECTION 6: CLOSING SECTION
       ========================================================== */
    .closing-section {
      padding: 110px 20px 95px;
      background: 
        radial-gradient(circle at 50% 30%, #ffffff 0%, rgba(250, 247, 242, 0.95) 55%, rgba(245, 238, 227, 0.8) 100%);
      text-align: center;
      position: relative;
    }

    .closing-ceremony-card {
      max-width: 660px;
      margin: 0 auto;
      padding: 55px 36px;
      background: rgba(255, 255, 255, 0.75);
      border: 1px solid var(--border-medium);
      border-radius: 6px;
      box-shadow: 
        0 20px 60px rgba(74, 14, 23, 0.07),
        inset 0 0 0 6px #ffffff,
        inset 0 0 0 7.5px var(--border-subtle);
      position: relative;
    }

    .closing-headline-warm {
      font-family: var(--font-names);
      font-size: clamp(36px, 7.5vw, 54px);
      color: var(--burgundy-deep);
      font-weight: 400;
      margin-bottom: 18px;
    }

    .closing-heartfelt-p {
      font-size: clamp(16px, 3.2vw, 19px);
      color: var(--text-editorial);
      line-height: 2.2;
      max-width: 540px;
      margin: 0 auto 30px;
    }

    .closing-signature-calligraphy {
      font-family: var(--font-names);
      font-size: clamp(42px, 8.5vw, 64px);
      color: var(--burgundy-main);
      font-weight: 400;
      margin: 12px 0 10px;
      display: inline-block;
      background: linear-gradient(135deg, #4a0e17 0%, #7d2633 45%, #912b3b 65%, #38070e 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 2px 6px rgba(74, 14, 23, 0.15));
    }

    /* Footer */
    .luxury-editorial-footer {
      padding: 35px 20px 30px;
      text-align: center;
      background: var(--ivory-paper);
      border-top: 1px solid var(--border-subtle);
      color: var(--text-light);
      font-size: 13.5px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      align-items: center;
    }

    .footer-actions-row {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      justify-content: center;
      margin-bottom: 8px;
    }

    .btn-footer-pill {
      color: var(--burgundy-main);
      font-size: 13px;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 7px 18px;
      border: 1px solid var(--border-medium);
      border-radius: 20px;
      background: #ffffff;
      box-shadow: 0 2px 8px rgba(74, 14, 23, 0.04);
      transition: all 0.3s ease;
    }

    .btn-footer-pill:hover {
      background: rgba(74, 14, 23, 0.05);
      color: var(--burgundy-deep);
      border-color: var(--champagne-gold);
      transform: translateY(-2px);
    }

    /* Scroll Reveal - Safe by default: ALWAYS visible */
    .reveal-item {
      opacity: 1;
      transform: translateY(0);
      transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1), transform 0.85s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Mobile */
    @media (max-width: 768px) {
      .section {
        padding: 75px 16px;
      }

      .opening-section {
        padding: 65px 14px 75px;
      }

      .editorial-hero-card {
        padding: 42px 18px 38px;
      }

      .event-spec-grid {
        grid-template-columns: 1fr;
        gap: 14px;
      }

      .notes-luxury-grid {
        grid-template-columns: 1fr;
        gap: 18px;
      }

      .venue-photograph-frame {
        height: 250px;
      }

      .countdown-capsule-row {
        gap: 10px;
      }

      .time-capsule {
        flex: 1 1 calc(50% - 10px);
        max-width: none;
        padding: 16px 8px;
      }

      .capsule-number {
        font-size: 40px;
      }

      .inner-letterpress-card {
        padding: 45px 20px 40px;
      }

      .mosque-metadata-banner {
        flex-direction: column;
        align-items: flex-start;
      }

      .floating-nav {
        top: 12px;
        left: 12px;
      }

      .pill-btn span.label-text {
        display: none;
      }
    }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }
  </style>
</head>
<body>

  <!-- Hidden SVG Symbols for soft 3D and botanical filigrees -->
  <svg style="display:none" aria-hidden="true">
    <symbol id="corner-filigree" viewBox="0 0 40 40">
      <path fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round"
        d="M2,38 L2,10 C2,5.6 5.6,2 10,2 L38,2 M6,34 L6,12 C6,8.7 8.7,6 12,6 L34,6 M10,10 L18,18" />
    </symbol>

    <symbol id="center-crest-flora" viewBox="0 0 200 40">
      <path fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"
        d="M10,20 Q60,5 90,20 Q95,5 100,5 Q105,5 110,20 Q140,5 190,20 M100,5 L100,35 M85,20 C85,15 95,15 100,20 C105,15 115,15 115,20" />
      <circle cx="100" cy="5" r="2.5" fill="currentColor" />
      <circle cx="70" cy="18" r="1.5" fill="currentColor" />
      <circle cx="130" cy="18" r="1.5" fill="currentColor" />
    </symbol>
  </svg>

  <!-- Luxury Framing Bars (Top and Bottom) -->
  <div class="luxury-frame-bar frame-bar-top" aria-hidden="true"></div>
  <div class="luxury-frame-bar frame-bar-bottom" aria-hidden="true"></div>

  <!-- Ambient Audio & WhatsApp Share Floating Buttons -->
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

  <!-- Delicate Falling Rose Petals Canvas -->
  <canvas id="petalsCanvas" aria-hidden="true"></canvas>

  <!-- ==========================================================
       SECTION 1: OPENING SECTION
       Arranged strictly vertically.
       First & most visually prominent element: The Names!
       ========================================================== -->
  <header class="opening-section" id="hero-opening">
    <div class="editorial-hero-card reveal-item is-visible">

      <!-- Corner Watermark Accents from burgundy texture -->
      <div class="corner-floral-watermark watermark-top-right" aria-hidden="true"></div>
      <div class="corner-floral-watermark watermark-bottom-left" aria-hidden="true"></div>

      <!-- Corner Filigrees -->
      <svg class="filigree-corner filigree-tr" aria-hidden="true"><use href="#corner-filigree" /></svg>
      <svg class="filigree-corner filigree-tl" aria-hidden="true"><use href="#corner-filigree" /></svg>
      <svg class="filigree-corner filigree-br" aria-hidden="true"><use href="#corner-filigree" /></svg>
      <svg class="filigree-corner filigree-bl" aria-hidden="true"><use href="#corner-filigree" /></svg>

      <!-- Monogram Crest -->
      <div class="monogram-crest-top">
        <div class="monogram-seal-disc" title="محمد & روجين">
          <span>م & ر</span>
        </div>
      </div>

      <!-- ----------------------------------------------------
           THE NAMES: FIRST AND MOST VISUALLY PROMINENT ELEMENT
           ---------------------------------------------------- -->
      <div class="grand-couple-hero">
        <h1 class="grand-couple-names">
          <span class="name-groom">محمد</span>
          <span class="couple-connector">&</span>
          <span class="name-bride">روجين</span>
        </h1>
        <div class="hero-names-subbar">
          <span>✦</span>
          <span>عقد قران مبارك</span>
          <span>✦</span>
        </div>
      </div>

      <!-- Center Botanical Flourish -->
      <svg style="width:170px; height:32px; margin:0 auto 12px; color:var(--champagne-gold); opacity:0.85;" aria-hidden="true">
        <use href="#center-crest-flora" />
      </svg>

      <!-- 1. Basmala -->
      <p class="bismillah-calligraphy" title="بسم الله الرحمن الرحيم">
        بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
      </p>

      <!-- 2. Formal Announcement Phrase -->
      <p class="invitation-formal-phrase">
        - نتشرف بدعوتكم لحضور حفل عقد قران
      </p>

      <!-- 3. Exact Lineage & Relationship -->
      <div class="lineage-card">
        <p class="lineage-text">
          <span class="highlight-groom">محمد</span>
          على كريمة السيد وائل،
          <span class="highlight-bride">روجين</span>
        </p>
      </div>

      <!-- 4. Heartfelt Greeting -->
      <p class="heartfelt-invitation-message">
        بقلوب يملؤها الفرح والسرور، يسعدنا دعوتكم لتشاركونا أجمل لحظات العمر، بحضوركم تكتمل فرحتنا.
      </p>

      <!-- 5. Prophetic Dua -->
      <div class="prophetic-dua-capsule">
        <span class="prophetic-dua-text">
          بارك الله لهما وبارك عليهما وجمع بينهما في خير
        </span>
      </div>

      <div class="divider-flourish" aria-hidden="true">
        <span>✤</span>
      </div>

      <!-- Scroll Action to Interactive Invitation -->
      <a href="#interactive-invitation" class="open-card-scroll-prompt" onclick="smoothScrollTo(event, '#interactive-invitation')">
        <span>افتحوا بطاقة الدعوة الخاصة</span>
        <div class="mouse-scroll-indicator">
          <div class="mouse-wheel-dot"></div>
        </div>
      </a>

    </div>
  </header>

  <!-- ==========================================================
       SECTION 2: INTERACTIVE INVITATION CARD
       A royal bespoke envelope in deep burgundy embossed floral
       relief that unfolds and opens when clicked!
       ========================================================== -->
  <section class="section interactive-section" id="interactive-invitation">
    <div class="container reveal-item">

      <div class="section-crest">
        <div class="crest-line"></div>
        <span class="crest-symbol">✦</span>
        <div class="crest-line left"></div>
      </div>

      <h2 class="section-title">بطاقة الدعوة الخاصة</h2>
      <p class="section-subtitle">
        المسوا الختم الملكي لفتح تفاصيل بطاقة الزفاف
      </p>

      <div class="envelope-theater" id="envelopeTheater">

        <!-- Outer Burgundy Folio Envelope -->
        <div class="burgundy-envelope">

          <!-- 3D Envelope Flaps Layer -->
          <div class="flap-container">
            <div class="flap-top" id="flapTop"></div>
            <div class="flap-left-angle"></div>
            <div class="flap-right-angle"></div>
          </div>

          <!-- 3D Wax Seal with Monogram -->
          <div class="wax-seal-center-stage" id="waxSealButton" onclick="toggleInvitationEnvelope()" role="button" tabindex="0" aria-label="اضغط لفتح بطاقة الدعوة">
            <div class="wax-seal-disc">
              <span class="seal-monogram-initials">م & ر</span>
            </div>
            <div class="seal-silk-ribbons">
              <div class="silk-tail left"></div>
              <div class="silk-tail right"></div>
            </div>
          </div>

          <!-- Pulsing Prompt Pill -->
          <button type="button" class="unfold-action-prompt" id="btnPromptUnfold" onclick="toggleInvitationEnvelope()">
            <span>انقر لفتح البطاقة</span>
            <span style="color:var(--champagne-gold); font-size:16px;">✦</span>
          </button>

          <!-- Inner Letterpress Invitation Card -->
          <article class="inner-letterpress-card" id="innerCardContent">
            
            <svg class="card-golden-header" aria-hidden="true">
              <use href="#center-crest-flora" />
            </svg>

            <p class="card-occasion-title">عقد قران مبارك</p>

            <h3 class="card-grand-names">محمد & روجين</h3>

            <p class="card-warm-message">
              يسعدنا ويشرفنا حضوركم ومشاركتكم فرحتنا الكبرى في هذه الليلة المباركة، متمنين أن يديم الله بيننا المحبة والمسرات في رحاب بيت من بيوت الله.
            </p>

            <div class="divider-flourish" style="margin: 16px auto; max-width: 160px;">
              <span>❦</span>
            </div>

            <div class="card-cta-group">
              <a href="#wedding-details" class="btn-card-primary" onclick="smoothScrollTo(event, '#wedding-details')">
                <span>عرض تفاصيل الموعد والمكان</span>
                <span>↓</span>
              </a>
              <button type="button" class="btn-card-outline" onclick="toggleInvitationEnvelope()">
                <span id="labelToggleEnvelope">طي البطاقة</span>
                <span>▲</span>
              </button>
            </div>

          </article>

        </div>

      </div>

    </div>
  </section>

  <!-- ==========================================================
       SECTION 3: WEDDING DETAILS & VENUE
       ========================================================== -->
  <section class="section section-cream" id="wedding-details">
    <div class="container reveal-item">

      <div class="section-crest">
        <div class="crest-line"></div>
        <span class="crest-symbol">❖</span>
        <div class="crest-line left"></div>
      </div>

      <h2 class="section-title">تفاصيل الحفل والمكان</h2>
      <p class="section-subtitle">
        موعدنا ولقاؤنا في رحاب هذا المكان المبارك بمشيئة الله
      </p>

      <article class="venue-grand-card">

        <!-- High Resolution Photograph of Al-Hosary Mosque -->
        <div class="venue-photograph-frame">
          <img 
            id="venueMosquePhoto"
            class="venue-actual-photo"
            src="assets/al-hosary-mosque.jpg"
            alt="صورة مسجد الحصري - ميدان الحصري، 6 أكتوبر، الجيزة"
            loading="lazy"
            decoding="async"
            onerror="this.onerror=null; this.src='https://upload.wikimedia.org/wikipedia/commons/4/45/Al-Hosary_Mosque_01.jpg';"
          >
          <div class="venue-photo-gradient-overlay"></div>
          <div class="venue-photo-tag">
            <span>مسجد الحصري</span>
            <span style="color:var(--champagne-gold)">✦</span>
            <span>مدينة 6 أكتوبر</span>
          </div>
        </div>

        <!-- Mosque Official Card Info with 5-Star Rating:
             Al-Hosary Mosque · ميدان الحصري, First 6th of October, Giza Governorate 12563, Egypt
             ★★★★★ · Mosque -->
        <div class="mosque-metadata-banner">
          <div class="mosque-official-meta">
            <strong>Al-Hosary Mosque · ميدان الحصري, First 6th of October, Giza Governorate 12563, Egypt</strong>
          </div>
          <div class="mosque-rating-cluster" title="تقييم 5 نجوم على خرائط Google">
            <span class="rating-stars-3d">★★★★★</span>
            <span class="rating-category-pill">· Mosque</span>
          </div>
        </div>

        <div class="venue-card-body">

          <h3 class="venue-headline-name">مسجد الحصري</h3>
          <p class="venue-detailed-address">
            ميدان الحصري، 6 أكتوبر، الجيزة
          </p>

          <!-- 2x2 Grid with SOFT 3D ICONS in Website Colors -->
          <div class="event-spec-grid">

            <!-- Detail 1: Date -->
            <div class="spec-capsule">
              <!-- Soft 3D Calendar Icon -->
              <div class="soft-3d-icon-box" aria-hidden="true">
                <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="calBg" x1="0" y1="0" x2="64" y2="64" gradientUnits="userSpaceOnUse">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#f0e6d6"/>
                    </linearGradient>
                    <linearGradient id="calHeader" x1="0" y1="0" x2="64" y2="20" gradientUnits="userSpaceOnUse">
                      <stop offset="0%" stop-color="#6e1d2a"/>
                      <stop offset="100%" stop-color="#4a0e17"/>
                    </linearGradient>
                    <linearGradient id="calRing" x1="0" y1="0" x2="0" y2="12" gradientUnits="userSpaceOnUse">
                      <stop offset="0%" stop-color="#e8ca88"/>
                      <stop offset="100%" stop-color="#9a7532"/>
                    </linearGradient>
                  </defs>
                  <rect x="9" y="15" width="46" height="42" rx="8" fill="#38070e" opacity="0.12"/>
                  <rect x="8" y="13" width="48" height="42" rx="7" fill="url(#calBg)" stroke="#c5a059" stroke-width="1.2"/>
                  <path d="M8 20C8 16.134 11.134 13 15 13H49C52.866 13 56 16.134 56 20V25H8V20Z" fill="url(#calHeader)"/>
                  <rect x="18" y="9" width="4" height="8" rx="2" fill="url(#calRing)"/>
                  <rect x="42" y="9" width="4" height="8" rx="2" fill="url(#calRing)"/>
                  <text x="32" y="44" font-family="'Aref Ruqaa', serif" font-size="18" font-weight="bold" fill="#4a0e17" text-anchor="middle">١٣</text>
                </svg>
              </div>
              <div class="spec-details">
                <p class="spec-label">اليوم والتاريخ</p>
                <p class="spec-val">الجمعة، 13 نوفمبر 2026</p>
              </div>
            </div>

            <!-- Detail 2: Time -->
            <div class="spec-capsule">
              <!-- Soft 3D Clock Icon -->
              <div class="soft-3d-icon-box" aria-hidden="true">
                <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <radialGradient id="clockBezel" cx="30%" cy="30%" r="70%">
                      <stop offset="0%" stop-color="#faeed6"/>
                      <stop offset="60%" stop-color="#c5a059"/>
                      <stop offset="100%" stop-color="#7d5e2a"/>
                    </radialGradient>
                    <radialGradient id="clockFace" cx="40%" cy="40%" r="60%">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#f6efe2"/>
                    </radialGradient>
                  </defs>
                  <circle cx="32" cy="34" r="23" fill="#38070e" opacity="0.14"/>
                  <circle cx="32" cy="32" r="23" fill="url(#clockBezel)"/>
                  <circle cx="32" cy="32" r="18.5" fill="url(#clockFace)" stroke="#d4af37" stroke-width="0.75"/>
                  <rect x="29" y="5" width="6" height="4" rx="1.5" fill="#c5a059"/>
                  <line x1="32" y1="32" x2="41" y2="32" stroke="#4a0e17" stroke-width="2.5" stroke-linecap="round"/>
                  <line x1="32" y1="32" x2="32" y2="43" stroke="#6e1d2a" stroke-width="2" stroke-linecap="round"/>
                  <circle cx="32" cy="32" r="2.5" fill="#4a0e17"/>
                </svg>
              </div>
              <div class="spec-details">
                <p class="spec-label">التوقيت</p>
                <p class="spec-val">الساعة 3:30 مساءً</p>
              </div>
            </div>

            <!-- Detail 3: Venue -->
            <div class="spec-capsule">
              <!-- Soft 3D Mosque Icon -->
              <div class="soft-3d-icon-box" aria-hidden="true">
                <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <linearGradient id="mosqueDome" x1="0" y1="15" x2="0" y2="45" gradientUnits="userSpaceOnUse">
                      <stop offset="0%" stop-color="#e8ca88"/>
                      <stop offset="60%" stop-color="#c5a059"/>
                      <stop offset="100%" stop-color="#8a6829"/>
                    </linearGradient>
                    <linearGradient id="mosqueWall" x1="0" y1="30" x2="0" y2="55" gradientUnits="userSpaceOnUse">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#f0e5d4"/>
                    </linearGradient>
                  </defs>
                  <path d="M32 12C23 18 20 28 20 36H44C44 28 41 18 32 12Z" fill="url(#mosqueDome)"/>
                  <circle cx="32" cy="10" r="2" fill="#e8ca88"/>
                  <path d="M32 6V10" stroke="#c5a059" stroke-width="1.5"/>
                  <rect x="18" y="36" width="28" height="18" rx="2" fill="url(#mosqueWall)" stroke="#c5a059" stroke-width="1"/>
                  <path d="M28 54V44C28 41.79 29.79 40 32 40C34.21 40 36 41.79 36 44V54H28Z" fill="#4a0e17"/>
                  <rect x="46" y="22" width="6" height="32" rx="1.5" fill="url(#mosqueWall)" stroke="#c5a059" stroke-width="0.8"/>
                  <path d="M49 14L46 22H52L49 14Z" fill="url(#mosqueDome)"/>
                </svg>
              </div>
              <div class="spec-details">
                <p class="spec-label">المكان</p>
                <p class="spec-val">مسجد الحصري</p>
              </div>
            </div>

            <!-- Detail 4: Address -->
            <div class="spec-capsule">
              <!-- Soft 3D Map Pin Icon -->
              <div class="soft-3d-icon-box" aria-hidden="true">
                <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <defs>
                    <radialGradient id="pinBody" cx="35%" cy="30%" r="70%">
                      <stop offset="0%" stop-color="#8e2b3c"/>
                      <stop offset="45%" stop-color="#58141f"/>
                      <stop offset="100%" stop-color="#38070e"/>
                    </radialGradient>
                    <radialGradient id="pinCore" cx="35%" cy="35%" r="65%">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#e8ca88"/>
                    </radialGradient>
                  </defs>
                  <ellipse cx="32" cy="54" rx="14" ry="4.5" fill="#38070e" opacity="0.2"/>
                  <path d="M32 52C32 52 46 36 46 25C46 16.716 39.732 10 32 10C24.268 10 18 16.716 18 25C18 36 32 52 32 52Z" fill="url(#pinBody)" stroke="#deb97a" stroke-width="1.2"/>
                  <circle cx="32" cy="24" r="7.5" fill="url(#pinCore)" stroke="#8a6829" stroke-width="0.8"/>
                  <circle cx="32" cy="24" r="3" fill="#4a0e17"/>
                </svg>
              </div>
              <div class="spec-details">
                <p class="spec-label">العنوان</p>
                <p class="spec-val">ميدان الحصري، 6 أكتوبر، الجيزة</p>
              </div>
            </div>

          </div>

          <!-- Clear Google Maps Directions Button -->
          <div class="maps-action-zone">
            <a 
              class="btn-google-directions"
              id="btnGoogleDirections"
              href="https://maps.app.goo.gl/gx99A4hY75tbNW6e8"
              target="_blank"
              rel="noopener noreferrer"
              title="فتح الموقع في خرائط Google للحصول على الاتجاهات"
            >
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
              <span>الاتجاهات عبر خرائط Google</span>
            </a>

            <p class="photo-credit-footnote">
              صورة المسجد: مسجد الحصري بمدينة السادس من أكتوبر (Wikimedia Commons CC)
            </p>
          </div>

        </div>

      </article>

    </div>
  </section>

  <!-- ==========================================================
       SECTION 4: ARABIC COUNTDOWN
       ========================================================== -->
  <section class="section countdown-section" id="wedding-countdown">
    <div class="container reveal-item">

      <div class="section-crest">
        <div class="crest-line"></div>
        <span class="crest-symbol">⌛</span>
        <div class="crest-line left"></div>
      </div>

      <h2 class="section-title">الوقت المتبقي حتى نلتقي</h2>
      <p class="section-subtitle">
        نعد الأيام والساعات بشوق ولهفة لمشاركتكم لحظات فرحتنا الكبرى
      </p>

      <!-- Live Arabic Countdown Capsules -->
      <div class="countdown-capsule-row" aria-live="polite">

        <div class="time-capsule">
          <span class="capsule-number" id="displayDays">--</span>
          <span class="capsule-unit">يوم</span>
        </div>

        <div class="time-capsule">
          <span class="capsule-number" id="displayHours">--</span>
          <span class="capsule-unit">ساعة</span>
        </div>

        <div class="time-capsule">
          <span class="capsule-number" id="displayMinutes">--</span>
          <span class="capsule-unit">دقيقة</span>
        </div>

        <div class="time-capsule">
          <span class="capsule-number" id="displaySeconds">--</span>
          <span class="capsule-unit">ثانية</span>
        </div>

      </div>

      <div class="countdown-live-badge" id="countdownStatusBadge">
        <span class="live-pulse-dot"></span>
        <span>العد التنازلي مباشر لموعد عقد القران المبارك</span>
      </div>

    </div>
  </section>

  <!-- ==========================================================
       SECTION 5: IMPORTANT NOTES
       ========================================================== -->
  <section class="section notes-section" id="important-guest-notes">
    <div class="container reveal-item">

      <div class="section-crest">
        <div class="crest-line"></div>
        <span class="crest-symbol">✦</span>
        <div class="crest-line left"></div>
      </div>

      <h2 class="section-title">ملاحظات تهم ضيوفنا</h2>
      <p class="section-subtitle">
        حرصًا منا على راحتكم وتيسير حضوركم في هذا اليوم الاستثنائي
      </p>

      <div class="notes-luxury-grid">

        <!-- Parking Note with Soft 3D Car Icon -->
        <article class="note-card-3d">
          <div class="note-header-3d">
            <div class="note-3d-icon" aria-hidden="true">
              <!-- Soft 3D Car SVG in Website Colors (Burgundy & Gold) -->
              <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                <defs>
                  <linearGradient id="carBody" x1="0" y1="20" x2="64" y2="45" gradientUnits="userSpaceOnUse">
                    <stop offset="0%" stop-color="#8e2b3c"/>
                    <stop offset="40%" stop-color="#58141f"/>
                    <stop offset="100%" stop-color="#38070e"/>
                  </linearGradient>
                  <linearGradient id="carWindow" x1="0" y1="20" x2="0" y2="32" gradientUnits="userSpaceOnUse">
                    <stop offset="0%" stop-color="#ffffff"/>
                    <stop offset="100%" stop-color="#edd9b8"/>
                  </linearGradient>
                  <radialGradient id="wheelRim" cx="35%" cy="35%" r="65%">
                    <stop offset="0%" stop-color="#fdfcf9"/>
                    <stop offset="70%" stop-color="#c5a059"/>
                    <stop offset="100%" stop-color="#4a0e17"/>
                  </radialGradient>
                </defs>
                <ellipse cx="32" cy="50" rx="22" ry="5" fill="#38070e" opacity="0.22"/>
                <path d="M8 38L14 27C16 23 20 21 25 21H39C44 21 48 23 50 27L56 38C58 40 58 44 56 46H8C6 44 6 40 8 38Z" fill="url(#carBody)" stroke="#deb97a" stroke-width="1.2"/>
                <path d="M16 28L20 23H44L48 28H16Z" fill="url(#carWindow)" opacity="0.9"/>
                <circle cx="13" cy="38" r="2.5" fill="#e8ca88"/>
                <circle cx="51" cy="38" r="2.5" fill="#e8ca88"/>
                <circle cx="18" cy="46" r="6.5" fill="#231417"/>
                <circle cx="18" cy="46" r="3.5" fill="url(#wheelRim)"/>
                <circle cx="46" cy="46" r="6.5" fill="#231417"/>
                <circle cx="46" cy="46" r="3.5" fill="url(#wheelRim)"/>
              </svg>
            </div>
            <h3 class="note-title-3d">موقف السيارات</h3>
          </div>
          <p class="note-content-p">
            نظرًا لاحتمالية وجود ازدحام مروري وصعوبة العثور على أماكن لركن السيارات، نرجو من حضراتكم مراعاة ذلك عند تحديد موعد الوصول.
          </p>
        </article>

        <!-- Separate Halls Note with Soft 3D Arches Icon -->
        <article class="note-card-3d">
          <div class="note-header-3d">
            <div class="note-3d-icon" aria-hidden="true">
              <!-- Soft 3D Separate Halls Dual Archways SVG in Website Colors -->
              <svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                <defs>
                  <linearGradient id="archGate" x1="0" y1="10" x2="0" y2="50" gradientUnits="userSpaceOnUse">
                    <stop offset="0%" stop-color="#ffffff"/>
                    <stop offset="100%" stop-color="#edd9b8"/>
                  </linearGradient>
                  <linearGradient id="innerGateDepth" x1="0" y1="20" x2="0" y2="48" gradientUnits="userSpaceOnUse">
                    <stop offset="0%" stop-color="#6e1d2a"/>
                    <stop offset="100%" stop-color="#38070e"/>
                  </linearGradient>
                </defs>
                <ellipse cx="32" cy="52" rx="22" ry="4" fill="#38070e" opacity="0.18"/>
                <path d="M12 48V28C12 21.37 16.48 16 22 16C27.52 16 32 21.37 32 28V48H12Z" fill="url(#archGate)" stroke="#c5a059" stroke-width="1.2"/>
                <path d="M16 48V29C16 24 18.69 20 22 20C25.31 20 28 24 28 29V48H16Z" fill="url(#innerGateDepth)"/>
                <path d="M32 48V28C32 21.37 36.48 16 42 16C47.52 16 52 21.37 52 28V48H32Z" fill="url(#archGate)" stroke="#c5a059" stroke-width="1.2"/>
                <path d="M36 48V29C36 24 38.69 20 42 20C45.31 20 48 24 48 29V48H36Z" fill="url(#innerGateDepth)"/>
                <circle cx="32" cy="14" r="2.5" fill="#c5a059"/>
              </svg>
            </div>
            <h3 class="note-title-3d">تنظيم القاعات</h3>
          </div>
          <p class="note-content-p">
            نود التنويه إلى أن قاعات الرجال والسيدات منفصلة، وذلك لضمان راحة جميع ضيوفنا.
          </p>
        </article>

      </div>

    </div>
  </section>

  <!-- ==========================================================
       SECTION 6: CLOSING SECTION
       ========================================================== -->
  <section class="section closing-section" id="closing-farewell">
    <div class="container reveal-item">
      <div class="closing-ceremony-card">

        <svg style="width:160px; height:32px; margin:0 auto 16px; color:var(--champagne-gold);" aria-hidden="true">
          <use href="#center-crest-flora" />
        </svg>

        <h2 class="closing-headline-warm">
          بوجودكم تكتمل فرحتنا
        </h2>

        <p class="closing-heartfelt-p">
          نسعد بحضوركم ومشاركتكم أجمل أيامنا، ونتمنى أن يجمعنا بكم دائمًا الخير والفرح.
        </p>

        <div class="divider-flourish" aria-hidden="true">
          <span>❦</span>
        </div>

        <div class="closing-signature-calligraphy">
          محمد & روجين
        </div>

      </div>
    </div>
  </section>

  <!-- Luxury Editorial Footer -->
  <footer class="luxury-editorial-footer">
    <div class="footer-actions-row">
      <!-- Add to Google Calendar -->
      <a 
        class="btn-footer-pill"
        href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=%D8%B9%D9%82%D8%AF+%D9%82%D8%B1%D8%A7%D9%86+%D9%85%D8%AD%D9%85%D8%AF+%D9%88%D8%B1%D9%88%D8%AC%D9%8A%D9%86&dates=20261113T133000Z/20261113T163000Z&details=%D9%86%D8%AA%D8%B4%D8%B1%D9%81+%D8%A8%D8%AF%D8%B9%D9%88%D8%AA%D9%83%D9%85+%D9%84%D8%AD%D8%B6%D9%88%D8%B1+%D8%B9%D9%82%D8%AF+%D9%82%D8%B1%D8%A7%D9%86+%D9%85%D8%AD%D9%85%D8%AF+%D9%88%D8%B1%D9%88%D8%AC%D9%8A%D9%86+%D8%A8%D9%85%D8%B3%D8%AC%D8%AF+%D8%A7%D9%84%D8%AD%D8%B5%D8%B1%D9%8A&location=%D9%85%D8%B3%D8%AC%D8%AF+%D8%A7%D9%84%D8%AD%D8%B5%D8%B1%D9%8A%D8%8C+%D9%85%D9%8A%D8%AF%D8%A7%D9%86+%D8%A7%D9%84%D8%AD%D8%B5%D8%B1%D9%8A%D8%8C+6+%D8%A3%D9%83%D8%AA%D9%88%D8%A8%D8%B1%D8%8C+%D8%A7%D9%84%D8%AC%D9%8A%D8%B2%D8%A9"
        target="_blank"
        rel="noopener noreferrer"
      >
        <span>📅</span>
        <span>إضافة الموعد إلى تقويم Google</span>
      </a>

      <!-- Smooth scroll to top -->
      <button type="button" class="btn-footer-pill" onclick="window.scrollTo({top:0, behavior:'smooth'})">
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
          elStatus.innerHTML = '<span class="live-pulse-dot"></span><span>اليوم هو يوم فرحتنا المبارك، مرحبًا بكم جميعًا!</span>';
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
       3. INTERACTIVE ENVELOPE UNFOLDING
       ---------------------------------------------------- */
    const envelopeTheater = document.getElementById("envelopeTheater");
    const labelToggleEnvelope = document.getElementById("labelToggleEnvelope");
    let isEnvelopeOpen = false;

    function toggleInvitationEnvelope() {
      isEnvelopeOpen = !isEnvelopeOpen;

      if (isEnvelopeOpen) {
        envelopeTheater.classList.add("is-opened");
        if (labelToggleEnvelope) labelToggleEnvelope.textContent = "طي البطاقة";
      } else {
        envelopeTheater.classList.remove("is-opened");
        if (labelToggleEnvelope) labelToggleEnvelope.textContent = "فتح البطاقة";
      }
    }

    // Keyboard support for wax seal
    const waxSealButton = document.getElementById("waxSealButton");
    if (waxSealButton) {
      waxSealButton.addEventListener("keydown", function(e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          toggleInvitationEnvelope();
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
       4. SCROLL REVEAL OBSERVER
       ---------------------------------------------------- */
    const revealItems = document.querySelectorAll(".reveal-item");
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: "0px 0px -40px 0px"
    });

    revealItems.forEach((item) => observer.observe(item));

    /* ----------------------------------------------------
       5. FALLING ROSE PETALS CANVAS ANIMATION
       ---------------------------------------------------- */
    const canvas = document.getElementById("petalsCanvas");
    const ctx = canvas.getContext("2d");
    let petals = [];
    const PETAL_COUNT = 18;

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
        this.y = initial ? Math.random() * canvas.height : -25;
        this.size = Math.random() * 8 + 6;
        this.speedY = Math.random() * 0.8 + 0.35;
        this.speedX = (Math.random() - 0.5) * 0.7;
        this.rotation = Math.random() * 360;
        this.rotationSpeed = (Math.random() - 0.5) * 1.6;
        this.opacity = Math.random() * 0.28 + 0.12;

        const isBurgundy = Math.random() > 0.45;
        this.color = isBurgundy
          ? `rgba(142, 43, 60, ${this.opacity})`
          : `rgba(228, 197, 124, ${this.opacity})`;
      }

      update() {
        this.y += this.speedY;
        this.x += Math.sin(this.y * 0.008) * 0.7;
        this.rotation += this.rotationSpeed;

        if (this.y > canvas.height + 25 || this.x < -30 || this.x > canvas.width + 30) {
          this.reset(false);
        }
      }

      draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate((this.rotation * Math.PI) / 180);
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.ellipse(0, 0, this.size * 0.55, this.size, 0, 0, Math.PI * 2);
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
       6. AMBIENT HARP SYNTHESIZER (WEB AUDIO API)
       Pure procedurally generated serenity - zero external asset!
       Muted by default to respect user choice.
       ---------------------------------------------------- */
    const btnAudio = document.getElementById("btnAmbientAudio");
    const audioSymbol = document.getElementById("audioSymbol");
    const audioLabelText = document.getElementById("audioLabelText");
    let audioContext = null;
    let isMelodyPlaying = false;
    let melodyTimer = null;

    const harpNotes = [293.66, 329.63, 349.23, 392.00, 440.00, 466.16, 523.25, 587.33, 659.25];

    function playSereneNote(frequency, duration = 2.8) {
      if (!audioContext) return;
      const osc = audioContext.createOscillator();
      const gain = audioContext.createGain();

      osc.type = "sine";
      osc.frequency.setValueAtTime(frequency, audioContext.currentTime);

      gain.gain.setValueAtTime(0.0001, audioContext.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.035, audioContext.currentTime + 0.12);
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
        playSereneNote(harpNotes[noteIdx], 3.2);

        if (beat % 2 === 0) {
          setTimeout(() => {
            if (isMelodyPlaying) {
              const chordIdx = (noteIdx + 4) % harpNotes.length;
              playSereneNote(harpNotes[chordIdx] * 0.5, 4.0);
            }
          }, 400);
        }
        beat++;
      }, 1600);
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
       7. SHARE VIA WHATSAPP / WEB SHARE API
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
    f.write(html_code)

with open('message.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("Successfully wrote index.html and message.html!")

