---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Allopurinol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Allopurinol：從痛風／高尿酸血症到肝性卟啉症

## 一句話總結

Allopurinol（別嘌醇）是黃嘌呤氧化酶抑制劑，一般用於痛風與高尿酸血症；本資料包未收錄其原適應症。
TxGNN 模型預測它可能對**肝性卟啉症 (Hepatic Porphyria)** 有效，但目前**沒有臨床試驗**，僅有 **2 篇間接文獻**，且兩篇都沒有以 allopurinol 為研究對象。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料包未提供（許可證的適應症欄位皆為空白） |
| 預測新適應症 | 肝性卟啉症 (Hepatic Porphyria) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5（資料包標為 L4，但所附文獻未涉及 allopurinol，實質上僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Allopurinol 已知的作用是抑制黃嘌呤氧化酶，降低尿酸生成。這個作用與肝臟血基質（heme）合成之間，並沒有已確立的關聯。

肝性卟啉症的核心問題在於肝臟 5-胺基酮戊酸合成酶（5-ALAS）被誘導、血基質合成失衡。目前檢索到的文獻只提出以色胺酸或抑制血基質利用來調控 5-ALAS 的假說，並未測試 allopurinol。

**這個高分需謹慎看待。** 前臨床研究曾指出 allopurinol 可能影響肝臟血基質與細胞色素 P450 的代謝，因此在提出任何再利用假說之前，必須先排除它誘發卟啉症發作的風險。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | 假說／綜述 | Medical Hypotheses | 提出以色胺酸或抑制色胺酸 2,3-雙加氧酶（TDO）的血基質利用，來調控 5-ALAS，作為急性肝性卟啉症的可能療法；未涉及 allopurinol |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | 動物研究 | Biochemical Pharmacology | 大鼠研究顯示 carbamazepine 會加劇血基質流失、惡化卟啉症；研究藥物為 carbamazepine，並非 allopurinol |

## 香港上市資訊

共 20 張許可證，以下列出 5 張主要許可證（資料包未提供劑型與核准適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-35846 | ALLOPURINOL TAB 100MG | HOVID LIMITED |
| HK-66571 | ALLOPURINOL TCK TABLETS 100MG | KAERU PHARMACEUTICAL (HK) LIMITED |
| HK-21594 | SYNPURINOL TAB 100MG | SYNCO (H.K.) LIMITED |
| HK-30121 | ALLOPURINOL TAB 100MG | CHRISTO PHARM LTD |
| HK-52620 | SYNORID TAB 100MG | SYNMOSA BIOPHARMA (HONG KONG) COMPANY LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 0.9995 的高分沒有任何 allopurinol 專屬的臨床或文獻證據支持，機轉上也缺乏合理連結。
- 前臨床線索反而提示可能有卟啉症誘發的安全疑慮。
- 其他預測適應症（肝門靜脈硬化、肝肺症候群、門靜脈血栓等）分數幾乎相同（約 0.9994），且都沒有證據，較可能是圖譜鄰近結構造成的假象。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料，這是目前的阻斷性缺口。
- 補齊 DrugBank 的作用機轉資料。
- 系統性檢視 allopurinol 對血基質合成、細胞色素 P450 及卟啉症的影響，先排除它誘發卟啉症的風險。
- 若安全性無疑慮，再檢索或設計 allopurinol 專屬的機轉研究與臨床證據。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

