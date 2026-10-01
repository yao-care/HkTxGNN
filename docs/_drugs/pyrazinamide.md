---
layout: default
title: Pyrazinamide
parent: 僅模型預測 (L5)
nav_order: 732
evidence_level: L5
indication_count: 5
---

# Pyrazinamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Pyrazinamide：從結核病到感染性中耳炎

## 一句話總結

Pyrazinamide 是抗結核多藥療法中的常用藥物，香港有 3 張許可證，但許可證資料未載明核准適應症。
TxGNN 模型預測它可能對**感染性中耳炎 (Infectious Otitis Media)** 有效，預測分數很高（99.96%）。
目前**沒有臨床試驗，也沒有直接對應的文獻**，這個預測僅來自模型。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 感染性中耳炎 (Infectious Otitis Media) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Pyrazinamide 是結核分枝桿菌專一的前驅藥，在酸性環境下轉化為 pyrazinoic acid 才有活性。對於肺炎鏈球菌、流感嗜血桿菌、卡他莫拉菌等一般細菌性中耳炎的常見病原，已知沒有抗菌活性。

這個預測合理的部分很有限。結核菌可引起結核性中耳炎，這是慢性化膿性中耳炎的罕見原因，抗結核藥物治療通常有效。因此，只有「經培養或 PCR 確認為結核菌感染」的那一小群病人，才可能用到 pyrazinamide，而且是作為多藥療法的一員。

高分較可能反映知識圖譜中「結核病」與「耳部感染」節點距離相近，不代表已驗證的藥理機轉。對一般細菌性中耳炎，沒有理由預期它有效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻（針對「感染性中耳炎」這個預測項目）。

以下是同一藥物其他預測適應症（慢性中耳炎、化膿性中耳炎）下的文獻，皆為結核性中耳炎的個案或小型病例系列，僅供參考，並非 pyrazinamide 專屬療效證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12680299](https://pubmed.ncbi.nlm.nih.gov/12680299/) | 2003 | Case series | Anales otorrinolaringologicos ibero-americanos | 報告 3 例結核性中耳炎；症狀與一般慢性中耳炎難以區分，常延遲診斷，抗結核藥物治療通常有效 |
| [15168420](https://pubmed.ncbi.nlm.nih.gov/15168420/) | 2004 | Case report | American Journal of Kidney Diseases | 腎臟移植受者的結核性中耳炎，先前反覆以經驗性抗生素治療無效 |
| [41783873](https://pubmed.ncbi.nlm.nih.gov/41783873/) | 2026 | Case report | Cureus | 以耳漏表現的結核性中耳炎，症狀不典型，在低盛行地區容易延遲診斷 |
| [18557517](https://pubmed.ncbi.nlm.nih.gov/18557517/) | 2008 | Case report | Irish Medical Journal | 9 歲女童的非結核分枝桿菌 (M. gordonae) 乳突炎，給予完整抗分枝桿菌治療後痊癒 |
| [41262919](https://pubmed.ncbi.nlm.nih.gov/41262919/) | 2025 | Case report | Frontiers in Pediatrics | 兒童眼眶顏面結核延伸至顱底，與中耳炎無直接關係 |
| [21532520](https://pubmed.ncbi.nlm.nih.gov/21532520/) | 2011 | 未分類 | Otology & Neurotology | 結核性中耳炎臨床表現多變，早期發現可改善治療結果 |
| [18852993](https://pubmed.ncbi.nlm.nih.gov/18852993/) | 2008 | 未分類 | Brazilian Journal of Otorhinolaryngology | 巴西結核性中耳炎增加；典型表現為鼓膜多處穿孔、耳漏與進行性聽力下降 |
| [11489368](https://pubmed.ncbi.nlm.nih.gov/11489368/) | 2001 | 未分類 | Auris Nasus Larynx | 年輕女性慢性耳漏、單側聽力喪失與反覆顏面神經麻痺，說明結核性中耳炎的診斷困難 |
| [1985808](https://pubmed.ncbi.nlm.nih.gov/1985808/) | 1991 | 未分類 | Deutsche Medizinische Wochenschrift | 多器官結核病例，同時有單側薦髂關節炎與頑固性耳痛，主題偏離中耳炎 |

這些文獻僅憑標題與摘要判讀，無法確認各案例實際使用的治療方案，需全文審閱。其中有些與主題不符，非結核分枝桿菌通常也對 pyrazinamide 不敏感。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-34750 | PYRAFAT TAB 500MG | MEKIM LTD |
| HK-06490 | PYRAZINAMIDE TAB 500MG | ATLANTIC PHARMACEUTICAL LIMITED |
| HK-26892 | RIFATER TAB | SANOFI HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症只有模型分數，沒有試驗或文獻支持（L5）。
- Pyrazinamide 只對結核分枝桿菌有活性，對一般細菌性中耳炎沒有預期療效。
- 相關文獻只涉及罕見的結核性中耳炎，且都是個案或小型病例系列。

**若要推進需要：**
- 取得香港衞生署的仿單，確認核准適應症與安全性資料（警語、禁忌）。
- 補齊作用機轉資料（可查詢 DrugBank）。
- 全文審閱結核性中耳炎的文獻，確認實際使用的抗結核方案與療效。
- 將適應症限縮為「經培養或 PCR 確認的結核性中耳炎」，並視為多藥療法的一部分。
- 若要往下走，先從系統性文獻回顧或回溯性病例整理開始，再考慮前瞻性研究。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

