---
layout: default
title: Ciprofloxacin
parent: 中證據等級 (L3-L4)
nav_order: 196
evidence_level: L4
indication_count: 10
---

# Ciprofloxacin
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

# Ciprofloxacin：從抗菌治療到瀰漫性硬皮症

## 一句話總結

Ciprofloxacin 是氟喹諾酮類（fluoroquinolone）抗菌藥，在香港已有 20 張許可證。
TxGNN 模型預測它可能對**瀰漫性硬皮症 (Diffuse Scleroderma)** 有效，但目前**沒有臨床試驗登記**，只有 **2 篇文獻**，且尚未看到明確的療效結果，屬於研究假說階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 瀰漫性硬皮症 (Diffuse Scleroderma) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。Ciprofloxacin 屬氟喹諾酮類抗菌藥，一般認為透過抑制細菌 DNA gyrase 與 topoisomerase IV 發揮殺菌作用。

硬皮症的特徵是微血管損傷、皮膚與內臟纖維化。模型未提供預測所依據的圖譜路徑，因此無法確認 TxGNN 的推論依據。

現有文獻提供兩個方向：

- 一篇 2010 年研究探討口服 ciprofloxacin 對硬皮症皮膚的抗纖維化作用。
- 另一篇探討系統性硬化症合併小腸細菌過度增生 (SIBO)，抗菌藥可能改善腸道症狀。

這兩篇都沒有顯示對皮膚或器官纖維化的疾病修飾效果。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | 對照研究（設計依標題與摘要推測，尚待確認） | J Dermatol | 評估口服 ciprofloxacin 是否降低硬皮症嚴重度，摘要提到採雙盲隨機對照設計。可取得的摘要被截斷，未見結果數據 |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | 診斷研究 | Br J Rheumatol | 24 位有吸收不良症狀的系統性硬化症患者，探討小腸細菌過度增生的偵測方法與治療結果。針對腸道症狀，並非皮膚纖維化 |

---

## 香港上市資訊

共 20 張許可證，以下列出 5 張：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-52577 | VIPROLOX 250 TAB 250MG | TRENTON-BOMA LTD |
| HK-53688 | LOXIN TAB 250MG | JEAN-MARIE PHARMACAL CO LTD |
| HK-51940 | ZOXAN-250 TAB 250MG | STAR MEDICAL SUPPLIES LTD |
| HK-47031 | POLI-CIFLOXIN 250 TAB 250MG | NATURAL HEALTH RESOURCES COMPANY LIMITED |
| HK-50313 | INTERFLOX 500 TAB 500MG | NATURAL HEALTH RESOURCES COMPANY LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測分數很高，加上 2 篇尚未看到明確療效結果的文獻，也沒有臨床試驗登記，證據等級為 L4。
- 現有文獻不足以說明 ciprofloxacin 對硬皮症皮膚或器官纖維化有實質益處。

**若要推進需要：**
- 取得 2010 年研究（PMID 20507401）全文，確認設計、樣本數與結果是否顯示抗纖維化效果。
- 釐清 TxGNN 預測的圖譜路徑與機轉依據。
- 補齊香港衛生署仿單的警語與禁忌資料，這是進入安全性篩選的前提。
- 評估長期使用氟喹諾酮的安全性與抗藥性風險。

**補充：同一藥物的其他預測**
在其他預測中，**敗血性鼠疫 (Septicemic Plague)** 的證據最強，為 L2，建議決策為 Proceed with Guardrails。該預測有一項已完成的 Phase 2 隨機非劣性試驗 ([NCT01243437](https://clinicaltrials.gov/study/NCT01243437)，200 人)，以及 2025 年發表於 NEJM 的腺鼠疫 RCT ([40768716](https://pubmed.ncbi.nlm.nih.gov/40768716/))。不過這些研究主要針對腺鼠疫，延伸到敗血型屬間接證據，且屬於抗菌藥用於其抗菌譜內的感染，並非機轉上的全新再利用。若要優先評估，建議以此項為主。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

