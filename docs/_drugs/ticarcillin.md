---
layout: default
title: Ticarcillin
parent: 僅模型預測 (L5)
nav_order: 862
evidence_level: L5
indication_count: 5
---

# Ticarcillin
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

# Ticarcillin：從細菌感染到淋巴結柵欄狀肌纖維母細胞瘤

## 一句話總結

Ticarcillin 是一種羧苄青黴素類（carboxypenicillin）抗生素，香港現有一張以複方（Ticarcillin 加 Clavulanic Acid）註冊的輸注用許可證。
TxGNN 模型預測它可能對**淋巴結柵欄狀肌纖維母細胞瘤 (Lymph Node Palisaded Myofibroblastoma)** 有效。
目前**沒有任何臨床試驗或文獻**支持，僅有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明適應症（本藥屬抗菌藥） |
| 預測新適應症 | 淋巴結柵欄狀肌纖維母細胞瘤 (Lymph Node Palisaded Myofibroblastoma) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ticarcillin 屬羧苄青黴素類抗生素，透過結合青黴素結合蛋白（PBP）來抑制細菌細胞壁合成。

淋巴結柵欄狀肌纖維母細胞瘤是良性腫瘤，沒有已知的細菌性致病因素。Ticarcillin 的抗菌機轉與這個疾病之間，**找不到合理的機轉連結**。這項預測目前只有 TxGNN 分數支持，較可能是知識圖譜的統計關聯，而非真實的藥理關係。

同批預測的其他四個適應症也有相同問題：

| 排名 | 預測適應症 | TxGNN 分數 | 評估 |
|------|-----------|-----------|------|
| 2 | 腹腔動脈壓迫症候群 (Celiac Trunk Compression Syndrome) | 99.82% | 屬機械性血管壓迫，抗菌藥無已知作用標的 |
| 3 | 腹部囊性淋巴管瘤 (Abdominal Cystic Lymphangioma) | 99.82% | 屬先天性淋巴畸形；治療囊腫繼發感染只是一般抗生素用途，不算老藥新用 |
| 4 | 腹腔異位妊娠 (Abdominal Ectopic Pregnancy) | 99.82% | 標準治療為手術或 methotrexate，青黴素類對滋養層細胞無已知作用 |
| 5 | 薦骨脊索瘤 (Sacrum Chordoma) | 99.82% | 由 brachyury (TBXT) 與 RTK 訊號驅動，Ticarcillin 無已知抗腫瘤機轉 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-63780 | TICARCILLIN AND CLAVULANIC ACID POWDER FOR SOLUTION FOR INFUSION 3.2G | JINDUN PHARMA (H.K.) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，沒有臨床試驗或文獻，也找不到合理的機轉連結。
- 預測的疾病多為良性腫瘤、先天畸形或機械性病變，與抗菌藥的作用機轉不相關，不建議投入資源。

**若要推進需要：**
- 補齊 Ticarcillin 的作用機轉資料（DrugBank）。
- 取得香港衛生署的仿單，確認警語與禁忌症。
- 找出任何支持抗菌機轉以外作用（如抗發炎、免疫調節）的前臨床證據。
- 目前沒有這類證據，建議先觀察，不主動推進。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

