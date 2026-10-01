---
layout: default
title: Mercaptopurine
parent: 中證據等級 (L3-L4)
nav_order: 556
evidence_level: L3
indication_count: 5
---

# Mercaptopurine
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

# Mercaptopurine：從抗代謝藥（原適應症資料缺漏）到骨髓性白血病

## 一句話總結

Mercaptopurine（6-MP）是嘌呤類抗代謝藥，香港有 2 張上市許可證，但許可證未載明原適應症。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效。
目前檢索到 **29 個臨床試驗**和 **20 篇文獻**，但多數是含 6-MP 的合併療法，且證據以急性前骨髓球性白血病 (APL) 維持治療為主，無法單獨評估 6-MP 的貢獻。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數 | 99.94%（排名 1826） |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料，以下機轉是依一般藥理知識推論。Mercaptopurine 是嘌呤類抗代謝藥，代謝產物硫代鳥嘌呤核苷酸 (thioguanine nucleotides) 會嵌入 DNA，並抑制嘌呤的從頭合成。這對快速增生的骨髓母細胞在機轉上說得通。

臨床上，6-MP 常作為維持治療的一環。APL 的 PETHEMA、GIMEMA、AIDA 類方案通常搭配 methotrexate 與 ATRA。較舊的 AML 誘導方案（如日本的 BHAC-DM）與老年 AML 維持方案也含 6-MP。極高的 TxGNN 分數與這些用法相符。

不過，證據多來自合併療法，且以 APL 為主，不等於對所有骨髓性白血病都有效。

---

## 臨床試驗證據

下表為 6-MP 明確出現在方案中、或與維持治療直接相關的試驗，共列 9 個。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | 完成 | 420 | 未治療 APL：比較加不加三氧化二砷的鞏固治療，並比較間歇 ATRA 與間歇 ATRA + mercaptopurine + methotrexate 的維持治療 |
| [NCT00002701](https://clinicaltrials.gov/study/NCT00002701) | Phase 3 | 未知 | 750 | ATRA + idarubicin 誘導、強化鞏固後，依微量殘存病灶隨機分派維持治療；6-MP 是否在方案內需查核 |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | 完成 | 105 | S0521：低/中風險 APL 的維持治療對觀察之隨機試驗；具體維持方案需查核 |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | 完成 | 300 | PETHEMA LPA2005：風險適應方案，維持治療為 ATRA + 低劑量化療（methotrexate + mercaptopurine） |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Phase 4 | 完成 | 未提供 | AIDA 風險適應方案，維持治療為 ATRA + methotrexate + mercaptopurine |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Phase 4 | 未知 | 80 | AIDA2000：風險適應 APL 治療，最後 2 年以 6-MP、methotrexate、ATRA 維持 |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | 未分期 | 未知 | 1068 | AIDA：檢驗間歇 ATRA、methotrexate + 6-MP 標準維持化療，或兩者併用 |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | 招募中 | 48 | 6-MP 或 hydroxyurea 合併 valproic acid，用於不適合標準療法的 AML 或高風險 MDS |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | 招募中 | 10 | Venetoclax 合併 6-MP 用於復發/難治型 AML（ApoAML） |

其餘試驗與 6-MP 的關聯不明或屬間接相關，未列入。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | RCT | Int J Hematol | JALSG-AML92：在 daunorubicin + behenoyl cytarabine + 6-MP 上加 etoposide，誘導治療無額外益處 |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | 隨機比較 | Cancer Chemother Pharmacol | 日本 58 家機構試驗，比較 daunorubicin 與 aclarubicin 搭配 BH-AC、6-MP、prednisolone；完全緩解率 63.7% 對 53.9% (P=0.0587) |
| [8558199](https://pubmed.ncbi.nlm.nih.gov/8558199/) | 1996 | 隨機試驗 | J Clin Oncol | 日本白血病研究組，比較 behenoyl cytarabine 與 cytarabine 的誘導與鞏固治療；摘要未列具體數據 |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | 世代研究 | J Korean Med Sci | 不適合移植的 AML 病人接受每日 6-MP + 每週 methotrexate 口服維持 2 年，評估無白血病存活與整體存活。背景指出維持化療過去未能提升治癒率 |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | 單臂試驗 | Cancer Invest | 兒童 AML 首次緩解期使用高劑量 6-MP + 中劑量 cytarabine 的可行性先導研究 |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | 單臂試驗 | Int J Hematol | 41 名成人 AML 接受 behenoyl cytarabine + daunorubicin + 6-MP 誘導，71% 達完全緩解 |
| [1657335](https://pubmed.ncbi.nlm.nih.gov/1657335/) | 1991 | 病例系列 | Chin Med J (Taipei) | 34 名成人 AML 接受 cytarabine + daunorubicin + 6-MP 誘導及鞏固化療 |
| [1059498](https://pubmed.ncbi.nlm.nih.gov/1059498/) | 1975 | 病例系列 | Cancer | 18 名兒童 AML 用四藥方案，初始緩解率 78%，中位存活 7 個月 |
| [24492035](https://pubmed.ncbi.nlm.nih.gov/24492035/) | 2014 | 回顧 | Rinsho Ketsueki | 日本 AML 與 APL 的現行治療回顧 |
| [28152123](https://pubmed.ncbi.nlm.nih.gov/28152123/) | 2017 | 世代研究 | JAMA Oncol | 自體免疫疾病治療與治療相關骨髓性腫瘤的關聯，屬安全性訊號而非療效證據 |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-03770 | PURI-NETHOL TAB | Aspen Pharmacare Asia Limited |
| HK-65479 | ALLMERCAP MERCAPTOPURINE ORAL SUSPENSION 20MG/ML | Link Healthcare Hong Kong Limited |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（嘌呤類抗代謝藥） |
| 骨髓抑制風險 | 依藥物類別判斷為中至高，實際請以仿單為準 |
| 致吐性分級 | 低（依口服抗代謝藥類別判斷） |
| 監測項目 | CBC（含分類）、肝功能、腎功能；可考慮 TPMT/NUDT15 基因型檢測 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

本資料包沒有 DrugBank 毒性資料，以上為依藥物類別的一般判斷。詳細警語請參考原廠仿單的警語與注意事項。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據集中在 APL 維持治療等合併方案，6-MP 的單獨貢獻無法確認。其餘骨髓性白血病的證據多為舊的單臂或病例研究。
- 仿單的警語與禁忌資料缺漏，且被標為阻擋性缺口，目前無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與核准適應症。
- 查詢 DrugBank 取得作用機轉。
- 逐一核對 NCT00002701、NCT00492856 等試驗方案中的 6-MP 角色與劑量。
- 把範圍收斂到 APL 維持治療，或不適合強化療的 AML，而非泛稱骨髓性白血病。
- 追蹤進行中的 NCT06199557 與 NCT05506332 的結果。

**其他預測適應症（皆建議 Hold）：**
- **CLL/SLL 及其亞型、肺母細胞瘤**（分數約 99.8%）：無任何試驗或文獻，僅為模型預測，證據等級 L5。
- **何杰金氏淋巴瘤**（99.80%）：檢索到的試驗都是淋巴母細胞性淋巴瘤、非何杰金氏淋巴瘤或 ALL。文獻多為 IBD 病人使用 thiopurine 的淋巴瘤風險，屬安全性訊號，與療效方向相反，證據等級 L4。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

