---
layout: default
title: Midazolam
parent: 中證據等級 (L3-L4)
nav_order: 575
evidence_level: L3
indication_count: 1
---

# Midazolam
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

# Midazolam：從注射鎮靜劑到失眠

## 一句話總結

Midazolam（咪達唑侖）在香港以注射劑型上市，目前記錄中沒有原適應症文字。
TxGNN 模型預測它可能對**失眠 (Insomnia)** 有效，預測分數 99.7%。
共檢索到 32 個臨床試驗登記和 11 篇文獻，其中只有少數直接相關：4 篇 1980 至 1990 年代的口服 midazolam 助眠臨床研究，以及 2 個以睡眠為結果指標的試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

DrugBank 的作用機轉欄位目前缺資料。以下藥理說明來自一般藥理知識，不是輸入資料。Midazolam 是苯二氮平類 (benzodiazepine)，作為 GABA-A 受體的正向異位調節劑，產生鎮靜與催眠作用。這個機轉與失眠治療直接相關，也符合模型給出的高分。

這個預測未必是真正的「新用途」。1981 至 1990 年間已有口服 midazolam 用於睡眠障礙的臨床研究，包括劑量探索研究和與 flurazepam 的 14 天比較。因此這個候選可能對應的是既有或歷史用途，而非全新適應症。

本次資料中的 `original_indications` 欄位是空的，9 張許可證中列出的 5 張也都沒有適應症文字。這很可能是資料缺漏，需要對照香港衛生署核准的仿單確認。

## 臨床試驗證據

以下列出與 midazolam 和睡眠最相關的試驗。其餘試驗多為右美托咪定、針灸、護理介入等，與本預測無直接關係。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | NA | 招募中 | 280 | 術前口服 midazolam 用於有睡眠障礙或焦慮的大腸直腸癌患者，觀察術後疼痛。族群與失眠有重疊，但主要終點不是失眠，尚無結果 |
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | 完成 | 111 | 比較右美托咪定與 midazolam 鎮靜後的術後睡眠品質。midazolam 是鎮靜對照，僅為間接支持 |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | NA | 已終止 | 5 | 以 24 小時睡眠多項生理檢查比較右美托咪定與 midazolam 對 ICU 病人睡眠的影響。僅收 5 人，資料極少 |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | 已終止 | 6 | 比較 α2 促效劑與 GABA 促效劑對睡眠階段的影響。僅收 6 人，資料極少 |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Phase 3 | 尚未招募 | 195 | 口服褪黑激素對比口服 midazolam 作為兒童扁桃腺切除術前用藥，觀察焦慮 |
| [NCT06480500](https://clinicaltrials.gov/study/NCT06480500) | Phase 2 | 招募中 | 110 | 以 midazolam 作為對照，測試氯胺酮加網路認知行為治療對難治型憂鬱症自殺意念的效果。與失眠無關 |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | 未知 | 120 | 右美托咪定對比 midazolam 用於重症通氣兒童的鎮靜 |
| [NCT04149626](https://clinicaltrials.gov/study/NCT04149626) | Phase 2 | 未知 | 60 | 骨科手術區域麻醉下，右美托咪定、midazolam、remifentanil 的鎮靜比較 |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | NA | 完成 | 23 | 右美托咪定對比 midazolam 用於 ICU 病人拔管前的鎮靜轉換 |

目前沒有任何已完成的 Phase 2/3 試驗，直接評估 midazolam 治療失眠。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | 臨床研究（雙盲） | Br J Clin Pharmacol | 30 位繼發於神經肌肉疾病的失眠女性，midazolam 15 mg 對比 Vesparax。兩者都有效，midazolam 耐受性較好，且沒有宿醉現象 |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | 臨床研究（劑量探索） | Arzneimittel-Forschung | 75 位住院的輕中度失眠患者，口服 midazolam 10–30 mg，多中心先導研究，評估療效與耐受性以找出最適劑量 |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | 臨床研究（隨機、雙盲、多中心） | J Clin Psychopharmacol | 慢性失眠患者使用 flurazepam 與 midazolam 14 天，觀察睡眠、表現與情緒。此篇為研究介紹，摘要中沒有結果 |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | 多中心臨床研究 | J Clin Psychopharmacol | 上述 14 天研究的執行摘要，無摘要內容可引用 |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatr Scand Suppl | 討論安眠藥的臨床使用與需要多種安眠藥的理由。苯二氮平類皆有臨床療效 |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | 臨床研究 | J Clin Med | Lemborexant 用於胰膽疾病患者內視鏡後的失眠與譫妄預防。主題不是 midazolam，僅為間接參考 |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | Orv Hetil | 失眠與腦部低灌流的關係，屬間接相關 |

## 香港上市資訊

香港共有 9 張許可證，以下列出 5 張。記錄中沒有劑型與核准適應症文字。

| 許可證號 | 品名 | 製造商 |
|---------|------|-------|
| HK-67778 | MIDAZ SOLUTION FOR INJECTION OR INFUSION 15MG/3ML | JACOBSON MARKETING LIMITED |
| HK-55150 | MIDAZOLAM INJ 1MG/ML (HAMELN) | MEKIM LTD |
| HK-25854 | DORMICUM INJ 5MG/ML | DKSH HONG KONG LIMITED |
| HK-20343 | DORMICUM INJ 15MG/3ML | DKSH HONG KONG LIMITED |
| HK-32941 | DORMICUM INJ 5MG/5ML | DKSH HONG KONG LIMITED |

從品名看，這 5 張都是注射劑型。歷史上的助眠研究用的是口服劑型，兩者之間有劑型落差。

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢結果為無資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉合理，且有 1980 至 1990 年代的口服 midazolam 助眠研究支持，但這些研究較舊，也沒有近期的 Phase 2/3 試驗。
- 香港上市的都是注射劑型，仿單的警語與禁忌資料缺漏（屬阻擋性缺口），無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌，並補齊安全性篩選所需資料。
- 補齊 DrugBank 的作用機轉資料。
- 確認是否已有口服劑型的核准或供應，並評估注射劑型用於失眠的可行性。
- 全文查證 1981 至 1990 年代的臨床研究設計與結果，並與現行安眠藥的證據比較。
- 追蹤 NCT06407518 的結果。

本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

