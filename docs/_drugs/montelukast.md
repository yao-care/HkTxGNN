---
layout: default
title: Montelukast
parent: 高證據等級 (L1-L2)
nav_order: 507
evidence_level: L2
indication_count: 5
---

# Montelukast
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Montelukast：從氣喘到支氣管炎

## 一句話總結

Montelukast 是白三烯受體（CysLT1）拮抗劑，原始核准適應症為氣喘（依 evidence pack 內部記載，非本次分析之新預測）。TxGNN 模型另外預測它可能對**支氣管炎（Bronchitis）**有效，目前有 **23 個臨床試驗**和 **20 篇文獻**支持這個方向，但其中相當比例與異體幹細胞移植後閉塞性細支氣管炎（GVHD/BOS）相關試驗經標記為與 montelukast 無直接關聯的雜訊。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 氣喘（依 evidence pack 內部文字記載為原始核准適應症；香港未上市，無許可證資料可佐證） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Montelukast 是選擇性 CysLT1（cysteinyl leukotriene receptor 1）拮抗劑，透過阻斷白三烯 D4 介導的氣道發炎、支氣管收縮與黏液分泌發揮療效——這是它在氣喘核准上市的核心機轉（DrugBank 未提供正式 MOA 文字，此描述引自 evidence pack 內部之機轉關聯性分析）。

白三烯路徑同樣參與嗜酸性球性支氣管炎（NAEB）及病毒誘發性支氣管痙攣的氣道發炎，因此 CysLT1 拮抗在理論上可能減緩發炎與黏液分泌，這是本預測機轉上的合理基礎。目前直接支持的證據集中在兩類：(1) NAEB／病毒性細支氣管炎的隨機對照試驗（如 NCT00863317、NCT01121016），顯示中等程度正面訊號；(2) 異體幹細胞移植後閉塞性細支氣管炎症候群（BOS）的小型 Phase 2 試驗（FAM 複方療法），顯示 montelukast 常以合併療法角色出現。

**需留意的限制**：本組候選試驗中有相當比例（如 ibrutinib、ruxolitinib、belumosudil 治療 GVHD 相關 bronchiolitis obliterans 的試驗）與 montelukast 並無直接關聯，屬疾病詞比對產生的雜訊，已由系統標記為 Grade C。此外，多數高品質證據其實針對「細支氣管炎（bronchiolitis）」而非典型成人「支氣管炎（bronchitis）」，兩者病理機轉與族群不完全相同，解讀時需注意用詞差異。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Phase 3 | 已完成 | 1125 | 比較兩劑量 MK0476（montelukast）與安慰劑，治療 3-24 個月大 RSV 細支氣管炎患兒之呼吸道症狀 |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | 未分期 | 已完成 | 141 | 雙盲安慰劑對照 RCT，評估每日口服 montelukast 對嬰兒首次病毒性細支氣管炎病程的影響 |
| [NCT03369119](https://clinicaltrials.gov/study/NCT03369119) | Phase 4 | 已完成 | 100 | 住院學齡前兒童急性氣喘發作，於標準治療外加口服 montelukast 的附加療效評估 |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Phase 4 | 狀態未明 | 63 | 雙盲安慰劑對照，評估 montelukast 加成吸入型 budesonide 治療非氣喘性嗜酸性球性支氣管炎（NAEB） |
| [NCT00524693](https://clinicaltrials.gov/study/NCT00524693) | 未分期 | 已完成 | 51 | 雙盲安慰劑對照 RCT，評估 montelukast 對急性 RSV 細支氣管炎臨床病程與細胞激素之影響 |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | 未分期 | 已完成 | 146 | 評估 montelukast 治療 3-12 個月嬰兒急性細支氣管炎及細支氣管炎後病毒誘發性喘鳴 |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | 已完成 | 25 | 多機構前瞻性研究，評估 montelukast 治療幹細胞移植後閉塞性細支氣管炎 |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Phase 2 | 已完成 | 36 | FAM 療法（fluticasone + azithromycin + montelukast）治療幹細胞移植後閉塞性細支氣管炎 |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | 已完成 | 30 | 雙盲安慰劑對照 RCT，評估 montelukast 減緩肺移植後閉塞性細支氣管炎症候群（BOS）進展 |
| [NCT02479074](https://clinicaltrials.gov/study/NCT02479074) | Phase 4 | 已完成 | 49 | 評估 montelukast 與 prednisolone 於慢性咳嗽鑑別診斷中，對咳嗽次數（feNO ≥30ppb 患者）之反應 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | RCT | Chinese Medical Journal | Montelukast 加成 budesonide 治療非氣喘性嗜酸性球性支氣管炎，改善氣道發炎、咳嗽與生活品質 |
| [20976161](https://pubmed.ncbi.nlm.nih.gov/20976161/) | 2010 | RCT | PLoS One | 隨機對照試驗比較魚油與 montelukast 對運動誘發支氣管收縮及氣道發炎之影響 |
| [24118637](https://pubmed.ncbi.nlm.nih.gov/24118637/) | 2014 | 系統性回顧 | Pediatr Allergy Immunol | 系統性回顧 montelukast 預防細支氣管炎後喘鳴之療效 |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | 回顧 | Ther Adv Respir Dis | 回顧 montelukast 治療肺／幹細胞移植後閉塞性細支氣管炎症候群（BOS）之潛力與可能機轉 |
| [38485149](https://pubmed.ncbi.nlm.nih.gov/38485149/) | 2024 | 臨床指引 | Eur Respir J | ERS/EBMT 臨床指引：成人肺部慢性移植物抗宿主病（cGVHD）治療 |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | 世代研究 | Respiratory Research | Budesonide/formoterol、montelukast 與 N-acetylcysteine 治療幹細胞移植後 BOS 之療效 |
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | 世代研究（Phase II） | Biol Blood Marrow Transplant | Fluticasone、azithromycin、montelukast（FAM）治療幹細胞移植後新發 BOS 之單臂多中心試驗 |
| [35114411](https://pubmed.ncbi.nlm.nih.gov/35114411/) | 2022 | Phase II 試驗 | Transplant Cell Ther | 前瞻性 Phase II 試驗評估 montelukast 治療幹細胞移植後 BOS，並探討其致病機轉 |
| [22819521](https://pubmed.ncbi.nlm.nih.gov/22819521/) | 2012 | 先導研究 | Respiratory Medicine | Montelukast 加成療法 vs 雙倍劑量 budesonide 治療非氣喘性嗜酸性球性支氣管炎之先導研究 |
| [16707408](https://pubmed.ncbi.nlm.nih.gov/16707408/) | 2006 | 藥動學研究 | J Clin Pharmacol | 評估 montelukast 於 3-6 個月大嬰兒之藥物動力學與安全性 |

---

## 香港上市資訊

目前 montelukast 在香港**未上市**，無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。（本次評估未能取得 TFDA/香港仿單警語與禁忌症資料，屬 Blocking 等級資料缺口，暫無法進行 S1 安全性初評。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 支氣管炎預測分數高（99.95%），且有明確機轉基礎與部分正向 RCT（如 NAEB、病毒性細支氣管炎試驗），但整體證據等級僅 L2，且候選試驗清單中混入大量 GVHD/幹細胞移植相關雜訊，需人工篩選確認真正相關子集。
- 仿單警語／禁忌症資料缺失（DG001，Blocking 等級），依規範無法進入 S1 安全性初評，這是目前推進的硬性阻礙。
- 香港尚無上市許可證，若要推進亦需先確認當地藥證與供應可行性。

**若要推進需要：**
- 取得 TFDA／香港仿單警語與禁忌症資料，解除 DG001 阻塞
- 補充 DrugBank 作用機轉（MOA）正式資料，取代目前引自 evidence pack 內部文字之描述
- 人工複核臨床試驗清單，剔除 GVHD/BOS 相關雜訊，聚焦真正的「支氣管炎／NAEB」適應症證據
- 釐清「bronchitis」與「bronchiolitis」在本候選中的用詞界線，避免適應症錯置
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

