---
layout: default
title: Salmeterol
parent: 高證據等級 (L1-L2)
nav_order: 675
evidence_level: L1
indication_count: 5
---

# Salmeterol
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Salmeterol：原適應症資料缺失 → 慢性支氣管炎 (Bronchitis)

## 一句話總結

> Salmeterol 在本次評估中缺乏香港原始適應症與正式 MOA 紀錄（未在香港上市，無許可證資料），但依證據包內文獻已知其為長效型 β2-腎上腺素受體促效劑（LABA）。
> TxGNN 模型預測它可能對**慢性支氣管炎 (Bronchitis)** 有效，
> 目前有 **16 個臨床試驗**和 **20 篇文獻**支持這個方向，其中多筆為 Phase 3 大型隨機對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（香港未上市，無許可證資料可查） |
| 預測新適應症 | 慢性支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 本候選之其他預測適應症

此評估包（candidate_id: TW-DB00938-multi）同時輸出 5 個 TxGNN 預測適應症，以下為總覽，供對照參考：

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 | 備註 |
|------|--------|-----------|---------|---------|------|------|
| 1 | 慢性支氣管炎 (Bronchitis) | 99.92% | L1 | S3 | Proceed with Guardrails | 本報告主要分析對象 |
| 2 | 呼吸道畸形 (Respiratory Malformation) | 99.91% | L4 | S0 | **Hold** | 附帶證據（氣喘/妊娠用藥/纖毛運動障礙個案）與病名明顯不符，疑為 KG 疾病本體映射錯置 |
| 3 | 阻塞性肺病 (Obstructive Lung Disease) | 99.89% | L1 | S3 | Proceed with Guardrails | COPD/氣喘上位概念詞，機轉直接對應 |
| 4 | Rienhoff Syndrome | 99.89% | L5 | S0 | **Hold** | 無任何臨床試驗或文獻支持，罕見結締組織疾病與 LABA 機轉無已知關聯 |
| 5 | 氣喘 (Asthma) | 99.78% | L1 | S3 | Proceed with Guardrails | 屬 Salmeterol 已知核心藥理用途，而非嚴格意義上的「新」適應症 |

**重要提醒**：排名 2（呼吸道畸形）與排名 4（Rienhoff syndrome）建議直接標記為擱置——證據包本身的 rationale 也指出這兩項極可能是 TxGNN 疾病節點映射錯誤，而非具臨床意義的老藥新用信號。以下章節聚焦於排名第一、證據最扎實的**慢性支氣管炎**。

---

## 為什麼這個預測合理？

目前官方仿單與 DrugBank 均未提供完整的作用機轉描述（標記為 Data Gap，屬 High 嚴重度缺口）。但依據證據包中文獻與試驗資料，Salmeterol 已知為**長效型 β2-腎上腺素受體促效劑（LABA）**，透過鬆弛支氣管平滑肌產生長效支氣管擴張作用，是氣喘與 COPD 臨床治療的核心機轉之一。

慢性支氣管炎（Chronic Bronchitis）在臨床上是 COPD 的一個常見亞型/併發表現，與氣道慢性發炎、黏液分泌過多及氣流受限密切相關。文獻 PMID 15970448 直接證實 salmeterol 可改善慢性支氣管炎患者的黏液纖毛清除與咳嗽清除能力，提供機轉層級的直接支持。此外，多個含 salmeterol 的複方製劑（如 fluticasone/salmeterol）在國際上已核准用於「COPD associated with chronic bronchitis」，顯示這項預測與現行臨床實務高度吻合，並非單純的模型外推。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Phase 3 | 完成 | 130 | Salmeterol/Fluticasone 50/500mcg BID vs 安慰劑，13 週雙盲比較支氣管抗發炎效果 |
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Phase 3 | 完成 | 584 | Salmeterol 與 Tiotropium 頭對頭六個月支氣管擴張療效與安全性比較 |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | 完成 | 741 | 大型多中心 COPD 支氣管擴張效果與安全性研究 |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | 完成 | 799 | 開放標籤長達 12 個月之慢性安全性研究 |
| [NCT01332409](https://clinicaltrials.gov/study/NCT01332409) | N/A | 完成 | 2000 | 日本上市後大規模用藥調查，COPD（含慢性支氣管炎/肺氣腫），肺炎為優先觀察指標 |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Phase 3 | 完成 | 122 | 標題明確針對「Chronic Bronchitis, Emphysema」之 56 週長期治療研究 |
| [NCT00633217](https://clinicaltrials.gov/study/NCT00633217) | Phase 4 | 完成 | 247 | FSC HFA MDI vs FSC DISKUS，劑量對應美國核准之「COPD associated with chronic bronchitis」適應症 |
| [NCT01110200](https://clinicaltrials.gov/study/NCT01110200) | Phase 4 | 完成 | 639 | ADVAIR DISKUS vs Salmeterol 單方，評估 COPD 住院後急性惡化率 |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Phase 3 | 完成 | 150 | 18 週兩藥物治療 COPD 比較試驗 |
| [NCT00857766](https://clinicaltrials.gov/study/NCT00857766) | Phase 4 | 完成 | 249 | FSC DISKUS 250/50mcg BID 對 COPD 患者動脈硬化度之 16 週研究 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | RCT | Pulm Pharmacol Ther | Salmeterol 改善輕中度慢性支氣管炎患者的黏液纖毛與咳嗽清除能力 |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | RCT | Clin Ther | 吸入型 Salmeterol 與口服 Theophylline 於輕中度 COPD 之療效、耐受性與生活品質比較 |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | RCT | Chest | FP/Salmeterol Diskus 合併製劑於 COPD 治療之療效與安全性 |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Cohort | Curr Med Res Opin | 慢性支氣管炎患者使用 FSC 起始維持治療之醫療利用與成本比較 |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline/Review | Basic Clin Pharmacol Toxicol | 芬蘭 COPD 穩定期診斷與藥物治療指引 |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Review | Drugs | Salmeterol/Fluticasone 於 COPD 之綜述，美國核准用於「COPD associated with chronic bronchitis」 |
| [16915216](https://pubmed.ncbi.nlm.nih.gov/16915216/) | 2006 | Review | MedGenMed | 吸入型 FSC (ADVAIR DISKUS) 250/50 治療 COPD 併慢性支氣管炎之病患經驗試驗結果 |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | Meta-analysis | Respir Res | Salmeterol 相較安慰劑/常規治療於 COPD 患者臨床結果改善之統合分析 |
| [21225021](https://pubmed.ncbi.nlm.nih.gov/21225021/) | 2010 | Review | Drugs of Today | 慢性支氣管炎與 COPD 患者肺功能下降與急性惡化風險，探討 Roflumilast 定位（COPD/慢性支氣管炎背景說明） |
| [10832348](https://pubmed.ncbi.nlm.nih.gov/10832348/) | 2000 | Review | MMW Fortschr Med | 吸菸相關慢性支氣管炎與肺氣腫之完整治療光譜建議 |

---

## 香港上市資訊

**香港上市狀態：未上市**（總許可證數：0）。目前無許可證資料可供列表，亦無法提取本地核准適應症文字。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（本次評估中，TFDA/香港仿單警語、禁忌症與 DDI 資料均標記為 Data Gap，其中仿單警語/禁忌屬 **Blocking** 等級缺口，將阻擋進入 S1 安全性初評。）

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅適用於慢性支氣管炎、阻塞性肺病、氣喘三項預測；呼吸道畸形與 Rienhoff syndrome 建議 Hold）

**理由：**
- 慢性支氣管炎預測獲得 L1 等級證據支持，包含多個 Phase 3 RCT（n 最高達 799）與大型上市後調查（n=2000），且 salmeterol 之 LABA 機轉與慢性支氣管炎/COPD 病理生理高度吻合，國際上亦已有相同成分複方核准用於此適應症。
- 香港尚未上市，且缺乏正式仿單安全性資料（Blocking data gap），在完成安全性初評前不宜逕行推進至臨床應用建議。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（Blocking，需下載仿單 PDF 解析）
- 透過 DrugBank API 補齊正式 MOA 文件，取代目前的機轉推論
- 若評估香港上市可行性，需準備完整藥品許可證申請資料
- 針對「呼吸道畸形」與「Rienhoff syndrome」兩項預測，建議先行覆核 TxGNN 疾病節點映射是否存在本體錯置問題，避免誤判為有效老藥新用信號
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

