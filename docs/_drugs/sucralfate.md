---
layout: default
title: Sucralfate
parent: 僅模型預測 (L5)
nav_order: 708
evidence_level: L5
indication_count: 2
---

# Sucralfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# SUCRALFATE：原始適應症資料缺失 → 預測十二指腸胃逆流 (Duodenogastric Reflux)

## 一句話總結

> Sucralfate（DrugBank DB00364）目前**未於香港上市**，Evidence Pack 中缺乏原始適應症與作用機轉（MOA）資料。
> TxGNN 模型預測它可能對**十二指腸胃逆流 (Duodenogastric Reflux)** 有效，
> 目前有 **13 篇文獻**支持，但**無相關臨床試驗登記**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（無許可證、`original_indications` 為空） |
| 預測新適應症 | 十二指腸胃逆流 (Duodenogastric Reflux) |
| TxGNN 預測分數 | 99.37%（rank 10605） |
| 證據等級 | L3（多篇觀察性研究/小型 RCT，但無正式登記之臨床試驗） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前 Evidence Pack 缺乏 Sucralfate 的作用機轉（MOA）與原始適應症資料（對應 DG002：MOA 缺失；DG001：仿單警語/禁忌缺失，屬 Blocking 等級）。

不過從既有文獻可觀察到機轉上的合理性：十二指腸胃逆流 (DGR) 的病理機轉是十二指腸內容物（含膽酸、胰液）逆流入胃，造成胃黏膜的化學性損傷（如 Nath & Warshaw 1984, PMID 6372664）。多篇 1985–2003 年的文獻直接測試了 sucralfate 於此類「鹼性逆流性胃炎 (alkaline reflux gastritis)」的療效，包括兩篇隨機對照試驗（Buch et al. 1985, PMID 3839973；Santarelli et al. 2003, PMID 12923369），顯示 sucralfate 的黏膜保護/膽酸吸附作用在此適應症下已有實際臨床觀察基礎，與 TxGNN 的預測方向一致。

換言之，這個預測並非單純模型外推，而是與既有（雖然年代較久的）臨床文獻相呼應。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3839973](https://pubmed.ncbi.nlm.nih.gov/3839973/) | 1985 | RCT | Am J Med | 隨機雙盲研究：sucralfate（6g/天）改善鹼性逆流性胃炎患者症狀與內視鏡/組織學表現 |
| [3475771](https://pubmed.ncbi.nlm.nih.gov/3475771/) | 1987 | RCT | Scand J Gastroenterol Suppl | 前瞻性隨機試驗，比較 sucralfate 與安慰劑用於胃炎（涵蓋十二指腸胃逆流相關型態） |
| [1391144](https://pubmed.ncbi.nlm.nih.gov/1391144/) | 1992 | RCT | Minerva Gastroenterol Dietol | 比較 cisapride 與 sucralfate 治療十二指腸胃逆流性胃炎相關消化不良 |
| [12923369](https://pubmed.ncbi.nlm.nih.gov/12923369/) | 2003 | RCT | Eur J Gastroenterol Hepatol | 隨機試驗比較 sucralfate、rabeprazole 與不治療，用於膽囊切除術後鹼性逆流性胃炎 |
| [17285081](https://pubmed.ncbi.nlm.nih.gov/17285081/) | 2006 | Review | J Chir | 十二指腸胃及胃食道膽汁逆流之病理生理、診斷（24小時膽汁監測）與治療現況回顧 |
| [14723838](https://pubmed.ncbi.nlm.nih.gov/14723838/) | 2004 | Review | Curr Treat Options Gastroenterol | 十二指腸胃逆流所致鹼性食道炎之藥物/手術治療選項回顧，PPI 為首選藥物治療 |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Annu Rev Med | 鹼性逆流性胃炎與食道炎之病理生理及診斷特徵回顧 |
| [10228771](https://pubmed.ncbi.nlm.nih.gov/10228771/) | 1999 | Review | Hepatogastroenterology | 十二指腸轉流手術治療病理性十二指腸胃逆流之適應症、技術與結果回顧 |
| [3838414](https://pubmed.ncbi.nlm.nih.gov/3838414/) | 1985 | Review | Am J Gastroenterol | 美國腸胃科醫學會委員會報告：sucralfate 於非潰瘍適應症（含胃炎、食道炎）之應用 |
| [3552846](https://pubmed.ncbi.nlm.nih.gov/3552846/) | 1987 | Review | Gastroenterol Clin Biol | 十二指腸胃逆流藥物治療之藥理學基礎（無摘要可用） |

---

## 香港上市資訊

目前無許可證資料（Sucralfate 未於香港上市，`total_licenses` = 0）

---

## 安全性考量

> 安全性資訊請參考原廠仿單。

⚠️ 需特別注意：此藥物的仿單警語與禁忌資料（DG001）標記為 **Blocking** 等級，現階段無法完成 S1 安全性初評，這是本次評估決策的主要限制因素。

---

## 結論與下一步

**決策：Hold**

**理由：**
- DG001（Blocking）：缺乏仿單警語/禁忌資料，導致本案無法進入 S1 安全性初評，屬硬性阻礙。
- Sucralfate 目前未於香港上市（0 張許可證），且新適應症無任何正式登記之臨床試驗，僅有 1985–2006 年間的歷史文獻（含 4 篇小型 RCT），證據等級為 L3。
- 原始適應症與 MOA 資料（DG002）皆缺失，機轉關聯性分析目前僅能依賴文獻內容推論，尚未經正式驗證。

**若要推進需要：**
- 取得 Sucralfate 完整仿單/藥品標籤資料（警語、禁忌、DDI），解除 DG001 blocking gap
- 補充 DrugBank 或其他來源的 MOA 與原始適應症資料（DG002）
- 若香港無上市計畫，評估其他地區（如已上市市場）之監管路徑作為輔助佐證
- 規劃前瞻性臨床試驗以更新此適應症的證據等級（現有 RCT 均為 1980–2000 年代小樣本研究）

**附註（其他候選適應症）：** 本輪預測另有 rank 2 候選「十二指腸阻塞 (duodenal obstruction, score 99.30%)」，經系統評估其機轉關聯薄弱（阻塞屬機械性/結構性問題，非黏膜化學性損傷），已判定為 **Hold**，研判為 TxGNN embedding 鄰近 peptic ulcer 所致之偽陽性，不建議進一步投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

