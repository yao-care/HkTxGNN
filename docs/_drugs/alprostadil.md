---
layout: default
title: Alprostadil
parent: 中證據等級 (L3-L4)
nav_order: 39
evidence_level: L3
indication_count: 10
---

# Alprostadil
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Alprostadil：從週邊動脈疾病到先天性主動脈畸形

## 一句話總結

Alprostadil 是前列腺素 E1（PGE1）的合成類似物，廣泛應用於週邊動脈疾病及導管依賴型先天性心臟病的術前緊急橋接治療。
TxGNN 模型預測它可能對**先天性主動脈畸形 (Aortic Malformation)** 有效，
目前有 **2 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 週邊動脈疾病 / 導管依賴型先天性心臟病橋接治療（香港無許可登記資料） |
| 預測新適應症 | 先天性主動脈畸形 (Aortic Malformation) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（evidence pack 標記為 Data Gap）。根據已知文獻，Alprostadil 是合成型 PGE1，其核心機轉為透過 EP2/EP4 受體活化 cAMP 訊號路徑，強力舒張動脈導管（ductus arteriosus）及週邊血管平滑肌，並兼具抗血小板聚集與抗炎效果。

先天性主動脈畸形（包含主動脈中斷 IAA 與重度主動脈縮窄）的新生兒，動脈導管往往是唯一維持體循環灌流的通道。PGE1 靜脈注射能有效阻止導管關閉、確保術前氧合與末稍灌流，是外科修復前不可或缺的橋接治療。這項應用自 1970 年代末即已在臨床確立（PMID 26686446），累積超過 40 年的實際使用紀錄。

TxGNN 的高預測分數（99.98%）與此豐富的歷史臨床依據高度一致，預測本身反映的是機轉上的高度合理性，而非純粹的圖譜拓撲推斷。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04054115](https://clinicaltrials.gov/study/NCT04054115) | Phase 1 | 已終止 | 10 | 直接評估 Alprostadil 於雙向 Glenn 術（BCPC）後對腦部與肺部血流的急性血液動力學效果；為唯一直接測試 PGE1 在複雜先天性主動脈/肺循環畸形中效果的登記試驗，雖因故提早終止，仍具高度相關性 |
| [NCT02042092](https://clinicaltrials.gov/study/NCT02042092) | Phase NA | 已完成 | 39 | 大血管血管炎患者彩色都卜勒超音波 vs 磁振血管造影的橫斷面比較研究，為診斷性影像研究，非 Alprostadil 療效評估，相關性有限，僅供解剖評估參考 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | RCT | Zhonghua Yi Xue Za Zhi | Alprostadil（Lipo-PGE1）與 Ulinastatin 顯著減輕先天性心臟病兒童體外循環後的炎症反應及肺損傷 |
| [26686446](https://pubmed.ncbi.nlm.nih.gov/26686446/) | 2015 | Clinical Review | Semin Thorac Cardiovasc Surg | PGE1 於 1970 年代末引入後，徹底改變主動脈中斷（IAA）的術前管理；支持一期修復前完整復甦策略 |
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | Prospective Clinical Series | Pharmacotherapy | PGE1 舒張動脈導管、增加肺血流，為多種類型先天性心臟畸形（含主動脈相關病型）的新生兒管理奠定藥理基礎 |
| [10771966](https://pubmed.ncbi.nlm.nih.gov/10771966/) | 1998 | Clinical Series | Indian J Pediatrics | PGE1 在導管依賴型先天性心臟病（含主動脈縮窄）新生兒第一階段緩和治療的印度臨床應用經驗 |
| [6537955](https://pubmed.ncbi.nlm.nih.gov/6537955/) | 1984 | Retrospective Series | J Am Coll Cardiology | 17 名新生兒長期 PGE1 靜脈輸注（平均 39 天，範圍 8-104 天），涵蓋主動脈縮窄病型，記錄療效、劑量與副作用 |
| [32184038](https://pubmed.ncbi.nlm.nih.gov/32184038/) | 2020 | Retrospective Cohort | Asian J Surgery | 主動脈中斷（IAA）分期手術修復的外科結果報告，PGE1 為術前穩定的標準用藥 |
| [25647388](https://pubmed.ncbi.nlm.nih.gov/25647388/) | 2014 | Clinical Protocol Review | Cardiology in the Young | 危急主動脈瓣狹窄新生兒術前管理方案，PGE1 為核心橋接用藥，詳述血液動力學管理策略 |
| [7201134](https://pubmed.ncbi.nlm.nih.gov/7201134/) | 1982 | Case Series | Pediatric Cardiology | PGE1 輸注用於低發育不全左心室合併主動脈閉鎖新生兒，6/7 例可見暫時性血液動力學改善 |
| [30347623](https://pubmed.ncbi.nlm.nih.gov/30347623/) | 2019 | Review/Cohort | J Neonatal-Perinat Med | 導管依賴型先天性心臟病新生兒在 PGE1 輸注期間的腸道餵食策略與壞死性腸炎（NEC）發生率分析 |
| [28508920](https://pubmed.ncbi.nlm.nih.gov/28508920/) | 2017 | Case Report | Pediatric Cardiology | 嚴重主動脈縮窄新生兒長期低劑量 PGE1 輸注期間發生二、三度房室傳導阻滯的罕見副作用報告 |

---

## 香港上市資訊

Alprostadil 目前在香港無任何上市許可登記（許可證數：0）。如需臨床使用，須透過特別用藥申請途徑辦理。

---

## 安全性考量

> 安全性資訊請參考原廠仿單。
>
> 根據現有文獻中記錄的常見副作用供參考：長期 PGE1 輸注可能引起骨皮質增生、幽門下瓣/胃竇黏膜增生（肥厚性幽門狹窄）、低血壓、呼吸暫停、發燒及心律不整（含房室傳導阻滯），詳細警語與禁忌症須查閱原廠仿單（TFDA 仿單資料目前缺漏，為 Blocking 資料缺口）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Alprostadil（PGE1）在先天性主動脈畸形（主動脈中斷 IAA、重度主動脈縮窄）的術前橋接治療中已有逾 40 年臨床使用歷史，多篇觀察性研究與臨床系列報告支持其核心機轉，TxGNN 預測分數高達 99.98%，機轉關聯極為清晰，屬 L3 證據等級。香港目前雖無上市許可，但此用途在國際上已有充分的臨床依據，具備推進法規申請的條件。

**若要推進需要：**
- 下載並解析 TFDA/原廠仿單 PDF，建立完整警語與禁忌症清單（DG001，Blocking 等級）
- 查詢 DrugBank API 取得系統性作用機轉資料（DG002，High 等級）
- 評估香港衛生署緊急用藥申請或臨床研究許可的法規途徑
- 制定特定族群（早產兒、不同主動脈畸形分型）的安全性監測計畫
- 考慮設計前瞻性觀察研究以積累在地臨床數據，將證據等級提升至 L2

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過嚴格臨床驗證方能應用於實際診療。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

