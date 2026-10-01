---
layout: default
title: Glucagon
parent: 中證據等級 (L3-L4)
nav_order: 410
evidence_level: L4
indication_count: 1
---

# Glucagon
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Glucagon：從原適應症（本次資料未提供）到腸躁症

## 一句話總結

Glucagon（升糖素）在香港有一張上市許可證，但本次資料沒有記載它的原適應症。
TxGNN 模型預測它可能對**腸躁症 (Irritable Bowel Syndrome)** 有效。
不過，目前沒有任何試驗直接測試 glucagon 用於腸躁症。現有臨床證據都來自 **GLP-1 受體促效劑**（如 ROSE-010），而不是 glucagon 本身。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 腸躁症 (Irritable Bowel Syndrome) |
| TxGNN 預測分數 | 99.24% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Glucagon 和 GLP-1 同源自 proglucagon 前驅物，兩者都會影響腸胃道動力，因此在藥物類別層級上，這個預測有一定合理性。

支持腸躁症方向的臨床訊號主要來自 GLP-1 類藥物。GLP-1 及其類似物 ROSE-010 已被報告能抑制腸道移動性收縮複合波、降低腸躁症患者的腸胃動力，並可能減輕發作時的疼痛。

但 glucagon 主要作用於升糖素受體，與 GLP-1 受體促效作用不同，GLP-1 的研究結果不能直接套用到 glucagon。TxGNN 的 0.992 分只是圖譜預測，缺少原適應症與機轉資料，也讓機轉推論更弱。

## 臨床試驗證據

以下為與腸躁症或腸道動力最相關的試驗，其餘試驗（飲食、益生菌、肥胖、類器官等）與 glucagon 無關，未列出。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | 完成 | 52 | ROSE-010（GLP-1 類似物）對便秘型腸躁症女性患者腸胃動力的影響。這是最接近腸躁症的臨床證據，但藥物不是 glucagon |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | 完成 | 12 | 天然 GLP-1 與 ROSE-010 對胃、十二指腸、空腸動力的抑制作用。支持動力機轉，但受試者非腸躁症患者 |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | 提前終止 | 8 | Liraglutide 用於迴腸袋肛門吻合術後、排便頻率高的患者。藥物不同，病況也只是與腸躁症相近 |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | NA | 完成 | 66 | 運動訓練對腸躁症患者腸道菌相與 GLP-1 荷爾蒙的影響。非藥物試驗 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT（次要分析） | Scand J Gastroenterol | ROSE-010 可減輕腸躁症發作時的疼痛，並分析最適合治療的族群 |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | 系統性回顧與統合分析 | Front Endocrinol | 探討 GLP-1 受體促效劑對腸躁症的改善作用 |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Exp Physiol | 探討腸道 L 細胞分泌的 GLP-1 在腸躁症病理生理中的角色 |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opin Investig Drugs | 便秘型腸躁症的新興研究藥物 |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Review | Ther Adv Gastroenterol | 腸躁症在纖維與解痙藥之外的治療選擇 |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review／觀點 | Adv Exp Med Biol | 噴霧型 GLP-1 用於糖尿病與腸躁症 |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | 世代研究 | Ann Gastroenterol | 腸躁症患者使用與停用 GLP-1 受體促效劑的處方模式 |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | 觀察性研究 | Clin Res Hepatol Gastroenterol | 便秘型腸躁症患者的 GLP-1 偏低，且與腹痛相關 |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | 動物研究 | Neurogastroenterol Motil | GLP-1 受體促效劑 exendin-4 改善腸躁症大鼠模型的腸胃功能障礙 |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | 臨床研究 | Front Nutr | 低 FODMAP 飲食後，腸躁症患者的循環 GLP-1 上升 |

以上文獻談的全是 GLP-1 軸，沒有 glucagon 本身用於腸躁症的研究。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-41845 | GLUCAGEN HYPOKIT FOR INJ 1MG/ML | NOVO NORDISK HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級只有 L4：TxGNN 預測分數高，但沒有任何試驗直接測試 glucagon，現有支持全部來自 GLP-1 類藥物，無法直接轉移。
- 原適應症、作用機轉與安全性資料都缺失，目前無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署核准的仿單，補齊警語、禁忌症與核准適應症。
- 補齊 DrugBank 的作用機轉資料，釐清 glucagon 與 GLP-1 在腸道動力上的差異。
- 尋找或設計 glucagon 直接用於腸躁症的研究（含文獻回顧或前臨床試驗）。
- 評估給藥途徑是否適用於腸躁症的長期治療。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

