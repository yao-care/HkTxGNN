---
layout: default
title: Hydroxyurea
parent: 中證據等級 (L3-L4)
nav_order: 380
evidence_level: L3
indication_count: 5
---

# Hydroxyurea
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# HYDROXYUREA：從既有血液腫瘤用藥到乳癌新適應症預測

## 一句話總結

> HYDROXYUREA（DrugBank DB01005）是核糖核苷酸還原酶（RNR）抑制劑，臨床上早已用於慢性骨髓性白血病、原發性血小板增多症、鐮形血球病等血液疾病（依文獻佐證；正式「原適應症」欄位為資料缺口）。
> TxGNN 模型針對此藥物產生 **5 個**新適應症預測，分數最高者為**乳癌 (Female Breast Carcinoma)**（99.97%），另外 4 個預測皆屬鐮形血球病相關基因型（HbSC、HbD、HPFH 合併鐮形血球病、HbS/β-地中海貧血）。
> 乳癌預測目前僅有 **0 個臨床試驗**及 **20 篇文獻**支持，證據多為早期合併化療 Phase I 研究與臨床前機轉研究（證據等級 L3）；相較之下，鐮形血球病族群（HbSC）已有 **11 個臨床試驗**（含 1 個 Phase 3 完成試驗）與 Cochrane 系統性回顧支持，證據等級達 L2。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 血液腫瘤／骨髓增生性疾病、鐮形血球病等（依文獻慣例；正式核准適應症紀錄為資料缺口） |
| 預測新適應症 | 乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question（研究假設階段） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）正式資料（DrugBank MOA 欄位為資料缺口，見 DG002）。但根據文獻佐證，Hydroxyurea 是核糖核苷酸還原酶（RNR）抑制劑，透過阻斷 DNA 合成前驅物（去氧核糖核苷酸）的生成，造成細胞週期 S 期特異性的抗增殖效果，並可誘發「replication stress」，使腫瘤細胞對 DNA 損傷路徑（如 ATR 抑制劑）更敏感。

乳癌屬於高度依賴細胞快速增殖與 DNA 複製的實體腫瘤，機轉上與 Hydroxyurea 的抗增殖作用具理論相容性。歷史上 Hydroxyurea 曾作為高劑量化療合併方案的成分之一（如 cyclophosphamide + thiotepa + HU 併自體幹細胞挽救、allopurinol + 5-FU + leucovorin + HU），用於轉移性乳癌的早期 Phase I/II 研究，顯示其在乳癌治療脈絡中並非全新概念。

近期研究更嘗試強化其乳癌應用潛力，例如以脂質共軛技術改善其親水性限制，並鎖定 PI3K/AKT/mTOR 路徑；另有多篇研究顯示 Valproic acid 等增敏劑可透過抑制 RPA2 過度磷酸化相關的 DNA 修復路徑，強化 Hydroxyurea 對乳癌細胞的殺傷力。然而，這些證據絕大多數屬於體外/臨床前研究或 1990 年代的早期合併療法試驗，**目前並無任何 ClinicalTrials.gov 登記之乳癌特異性 Hydroxyurea 試驗**，機轉合理性尚待現代臨床研究驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7914447](https://pubmed.ncbi.nlm.nih.gov/7914447/) | 1994 | Phase I/II（合併療法） | Bone Marrow Transplant | 高劑量 cyclophosphamide + thiotepa + HU 併自體幹細胞挽救，作為轉移性乳癌緩解後的鞏固化療方案 |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase I（合併療法） | Am J Clin Oncol | Allopurinol + 5-FU + Leucovorin，續以 HU 治療，用於晚期腸胃道及乳癌患者（HALF regimen） |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | 機轉／分子生物學 | DNA Repair | Valproic acid 透過抑制 RPA2 過度磷酸化相關 DNA 修復路徑，增敏乳癌細胞對 HU 的反應 |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | 臨床前（體外） | DNA Repair | 2-hexyl-4-pentynoic acid 可作為 valproic acid 替代品，經由相同 RPA2 機轉增敏乳癌細胞對 HU 之反應 |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | 電腦模擬／臨床前 | Drug Research | 設計 HU 脂質共軛物以改善親水性限制，鎖定 PI3K/AKT/mTOR 路徑治療乳癌 |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | 臨床前（體外） | Mol Pharmacol | 新型 RNR 抑制劑 COH29 抑制 DNA 修復，並與 HU 同機轉比較於 BRCA1 缺陷型乳癌細胞 |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | 臨床前（體外） | Br J Cancer | ATR 抑制劑 NU6027 於乳癌及卵巢癌細胞株中增強對複製壓力相關藥物之敏感性 |
| [26844848](https://pubmed.ncbi.nlm.nih.gov/26844848/) | 2016 | 臨床前（顯影劑開發） | Cancer Biother Radiopharm | 以鎝-99m 標記 HU 開發顯影劑，文中確認 HU 為治療白血病、鐮形血球病等之抗腫瘤藥物 |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | 個案報告 | Case Rep Hematol | 乳癌合併原發性血小板增多症患者，說明 HU 用於血小板增多症治療之臨床挑戰 |
| [28585003](https://pubmed.ncbi.nlm.nih.gov/28585003/) | 2017 | 個案報告 | Breast Cancer (Tokyo) | 慢性骨髓性白血病患者以 HU + imatinib 治療緩解後，四年後續發乳管原位癌之個案 |

---

## 細胞毒性

**判斷依據**：Hydroxyurea 為已知之抗代謝物類細胞毒性藥物，臨床用於白血病、鐮形血球病等惡性/血液疾病，且本評估之預測新適應症（乳癌）本身即為惡性腫瘤。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（核糖核苷酸還原酶 RNR 抑制劑，抗代謝物類） |
| 骨髓抑制風險 | 高（S 期特異性抑制 DNA 合成，為劑量限制性毒性，常見嗜中性白血球減少與巨球性貧血） |
| 致吐性分級 | 低（口服製劑，致吐性通常屬低度） |
| 監測項目 | 全血球計數（CBC，含白血球分類）、腎功能、肝功能 |
| 處置防護 | 屬細胞毒性藥物，操作應依細胞毒性藥物處置規範進行；惟正式仿單警語尚未取得（見下方安全性資料缺口） |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 資料缺口提示：本評估之 TFDA/HK 仿單警語與禁忌症查詢結果為 **Blocking 等級資料缺口（DG001）**，在取得正式仿單資料前，無法完成 S1 安全性初評，請優先處理。

---

## 附錄：其他預測適應症總覽

本 Evidence Pack 屬多適應症（multi）候選案，除乳癌外，TxGNN 同時對以下 4 個鐮形血球病相關基因型產出高分預測，證據成熟度與建議決策階段列表如下：

| Rank | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議決策 | 關鍵佐證 |
|------|-----------|-----------|---------|---------|---------|---------|
| 2 | Sickle Cell–Hemoglobin C Disease | 99.67% | L2 | S3 | Proceed with Guardrails | 11 個臨床試驗（含 Phase 3 完成之 NOHARM 試驗 NCT03128515, n=187）+ 2 篇 Cochrane 系統性回顧 |
| 3 | Sickle Cell–Hemoglobin D Disease | 99.67% | L4 | S1 | Research Question | 僅個案報告與一般 SCD 族群間接推論，無 HbD 特異性試驗 |
| 4 | HPFH 合併鐮形血球病 | 99.67% | L5 | S0 | Hold | 無直接相關試驗或文獻，僅為模型預測性關聯 |
| 5 | Sickle Cell–β-地中海貧血 | 99.67% | L2 | S2 | Research Question | 1999 年 RCT（[PMID 10326220](https://pubmed.ncbi.nlm.nih.gov/10326220/)）納入此亞型病例 |

值得注意的是，Hydroxyurea 誘導胎兒血紅蛋白（HbF）以降低紅血球鐮狀化的機轉，在鐮形血球病譜系（rank 2、3、5）具高度一致性，且 rank 2（HbSC）已達到「Proceed with Guardrails」等級，證據成熟度明顯高於乳癌預測。

---

## 結論與下一步

**決策：Hold（研究假設階段，對應乳癌預測之 Research Question）**

**理由：**
- 乳癌預測（本報告主軸）目前無任何臨床試驗支持，僅有臨床前機轉研究與 1990 年代早期合併療法 Phase I 研究，證據等級僅達 L3，尚不足以支持臨床推進。
- 相對而言，同一藥物對鐮形血球病族群（尤其 HbSC）的預測已有 Phase 3 完成試驗與系統性回顧支持（L2），顯示 Hydroxyurea 於此適應症方向的再驗證價值更高，建議優先評估。

**若要推進需要：**
- **補齊 Blocking 資料缺口 DG001**：取得 TFDA/HK 正式仿單警語與禁忌症資料，此為進入 S1 安全性初評之前提。
- **補齊 High 資料缺口 DG002**：透過 DrugBank API 查詢完整作用機轉（MOA），以強化機轉關聯性分析之嚴謹度。
- 針對乳癌方向：規劃現代化臨床前驗證（如異種移植模型）以確認 HU 與增敏劑併用之療效，並評估是否有必要啟動早期臨床試驗。
- 針對鐮形血球病方向：確認 Hydroxyurea 在香港（或目標市場）之上市/註冊狀態，並評估是否可直接依現有國際證據申請適應症擴充，而非以「全新藥物再利用」路徑處理。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

