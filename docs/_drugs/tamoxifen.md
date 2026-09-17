---
layout: default
title: Tamoxifen
parent: 中證據等級 (L3-L4)
nav_order: 720
evidence_level: L4
indication_count: 10
---

# Tamoxifen
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Tamoxifen：從乳癌到乳房佩吉特氏病

## 一句話總結

Tamoxifen 是一種選擇性雌激素受體調節劑（SERM），核心藥理作用為競爭性結合雌激素受體（ER），已知核准用途為 ER 陽性乳癌之治療與預防。
TxGNN 模型預測它可能對**乳房佩吉特氏病（Mammary Paget Disease）**有效，
目前有 **1 個間接相關臨床試驗**和 **13 篇文獻**（多為個案報告與小型世代研究）支持這個方向，證據等級偏低（L4）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乳癌（ER 陽性）— 香港許可證資料缺失，此為 Tamoxifen 已知核准用途 |
| 預測新適應症 | 乳房佩吉特氏病 (Mammary Paget Disease) |
| TxGNN 預測分數 | 99.69% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Tamoxifen 詳細作用機轉的結構化資料（DrugBank MOA 查詢為空）。根據已知藥理學知識與本證據包內文獻／試驗描述可交叉確認，Tamoxifen 為 SERM，透過競爭性結合雌激素受體、抑制 ER 訊號驅動之腫瘤生長，此機轉已於 ER 陽性乳癌中被廣泛證實。

乳房佩吉特氏病（Mammary Paget Disease）是一種罕見的乳頭表皮內病變，90% 以上病例合併潛在的乳管癌（多為 ER 陽性）。Tamoxifen 的抗雌激素機轉理論上可作用於合併之乳癌成分，這也是 TxGNN 產生此預測的合理基礎。

然而，Paget 氏病本身（表皮內 Paget 細胞）並非典型的雌激素依賴性病灶，目前沒有直接證據顯示 Tamoxifen 對 Paget 細胞本身具有治療機轉。現有臨床試驗（NCT00002920）僅涉及背景族群重疊（同一試驗收案族群包含 Paget's disease 患者，但試驗本身測試的是 MPA 預防子宮內膜病變，並非測試 Tamoxifen 治療 Paget 氏病），文獻證據也以個案報告與小型世代研究為主，尚無針對此適應症的前瞻性試驗。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00002920](https://clinicaltrials.gov/study/NCT00002920) | Phase 3 | 已完成 | 313 | 收案族群包含 Paget's disease 患者，但試驗本身測試 medroxyprogesterone 在服用 tamoxifen 之停經後乳癌患者中預防子宮內膜病變的效果，**非**直接測試 tamoxifen 治療 Paget 氏病（相關性評級：C，背景族群重疊而非直接證據） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34463889](https://pubmed.ncbi.nlm.nih.gov/34463889/) | 2022 | Case Report | Investigational New Drugs | 荷爾蒙受體陽性轉移性乳腺外 Paget 氏病以 tamoxifen 治療成功案例 |
| [14965622](https://pubmed.ncbi.nlm.nih.gov/14965622/) | 2001 | Case Report | Breast (Edinburgh) | 廣泛乳頭 Paget 氏病案例，以 Tamoxifen 治療獲得部分反應 |
| [1648987](https://pubmed.ncbi.nlm.nih.gov/1648987/) | 1991 | Review | British Journal of Surgery | 48 例乳頭 Paget 氏病回顧性分析，其中 1 例以 tamoxifen 治療 |
| [16277886](https://pubmed.ncbi.nlm.nih.gov/16277886/) | 2005 | Cohort | Clinical Breast Cancer | 保乳治療後局部復發表現為乳頭 Paget 氏病之世代研究 |
| [25759627](https://pubmed.ncbi.nlm.nih.gov/25759627/) | 2014 | Meta-Analysis | Breast Care (Basel) | 乳房切除術 vs. 保乳手術治療 Paget 氏病後局部復發率統合分析 |
| [8955252](https://pubmed.ncbi.nlm.nih.gov/8955252/) | 1996 | Case Report | American Surgeon | 男性乳房 Paget 氏病組織學確診案例，回顧全球 32 例文獻 |
| [29694313](https://pubmed.ncbi.nlm.nih.gov/29694313/) | 2018 | Case Report | Il Giornale di Chirurgia | 男性乳頭 Paget 氏病案例報告 |
| [12924421](https://pubmed.ncbi.nlm.nih.gov/12924421/) | 2003 | Case Report | Surgery Today | 同時性雙側乳癌合併 Paget 氏病與浸潤性導管癌案例 |
| [19112575](https://pubmed.ncbi.nlm.nih.gov/19112575/) | 2009 | Case Report | Archives of Gynecology and Obstetrics | 外陰與乳房 Paget 氏病合併潛在癌症之罕見案例 |
| [17319355](https://pubmed.ncbi.nlm.nih.gov/17319355/) | 2006 | Case Series | Nigerian Journal of Clinical Practice | 奈及利亞乳頭-乳暈複合體 Paget 氏病 8 例臨床特徵分析 |

---

## 香港上市資訊

Tamoxifen 目前**未於香港上市**（許可證登記數：0 張）。無可提取之許可證明細或核准適應症文字。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 荷爾蒙類抗腫瘤藥物（SERM），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 低（SERM 機轉不同於傳統細胞毒素，本證據包無 toxicity 明細資料） |
| 致吐性分級 | 低 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
乳房 Paget 氏病與 Tamoxifen 的機轉連結建立在「Paget 氏病常合併潛在 ER+ 乳管癌」的間接推論上，Paget 細胞本身並非典型雌激素依賴病灶；現有證據以個案報告與小型回顧性研究為主（最高僅達 Cohort/Meta-analysis 層級），缺乏針對此適應症的前瞻性試驗，TxGNN 評分之決策階段亦標註為 S1（Research Question）。此外藥物在香港尚未上市，仿單警語、禁忌症資料（DG001，Blocking）與作用機轉資料（DG002，High）均缺失，無法完成安全性初評。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking，來源：官方仿單 PDF 解析）
- 補齊 DrugBank 作用機轉資料（DG002，High），釐清機轉關聯性
- 針對乳房 Paget 氏病設計前瞻性臨床研究，驗證療效假說
- 確認香港上市規劃與許可證申請路徑（目前 0 張許可證）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

