---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Colchicine：預測新適應症為惡性瘧原蟲瘧疾 (Plasmodium falciparum malaria)（證據等級 L5）。原適應症：痛風、家族性地中海熱"
monitor_inn: "COLCHICINE"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Colchicine：從痛風到瘧疾（惡性瘧原蟲 Plasmodium falciparum malaria）
{: .text-alpha }

## 一句話總結

Colchicine（秋水仙素）原本用於治療痛風與家族性地中海熱。
TxGNN 模型預測它可能對**惡性瘧原蟲瘧疾 (Plasmodium falciparum malaria)** 有效，但目前**沒有臨床試驗**，僅有 **2 篇間接相關的前臨床文獻**，證據非常薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 痛風、家族性地中海熱 |
| 預測新適應症 | 惡性瘧原蟲瘧疾 (Plasmodium falciparum malaria) |
| TxGNN 預測分數 | 99.60% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 colchicine 是微管破壞劑，會抑制微管蛋白（tubulin）聚合，並影響嗜中性白血球趨化與發炎反應，因此在痛風與家族性地中海熱中有療效。

在瘧疾方面，機轉上的連結只是推測：其他微管干擾物（例如薑黃素）曾被發現會破壞瘧原蟲的微管，顯示微管可能是寄生蟲的弱點。另一篇文獻探討 pfmdr1 基因在哺乳動物細胞中的表現與藥物敏感性，可能與 colchicine 作為 P-醣蛋白受質有關。不過這兩篇都沒有顯示 colchicine 本身對瘧疾有效。

此外，colchicine 治療指數窄，對宿主細胞也有毒性，要用於抗瘧疾相當有疑慮。0.996 的高分是模型的計算預測，不等於臨床證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | 體外／前臨床 | PloS one | 研究對象為薑黃素而非 colchicine；發現薑黃素會破壞惡性瘧原蟲的微管 |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | 體外／前臨床 | Molecular and cellular biology | pfmdr1 基因在哺乳動物細胞中表現，與對氯喹的敏感性增加有關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37807 | COLGOUT TAB 0.5MG | 未提供 | 未提供 |
| HK-60077 | COLCHICINE TAB 0.5MG | 未提供 | 未提供 |
| HK-44403 | COLCHICINE TAB 500MCG (SYNCO) | 未提供 | 未提供 |
| HK-66396 | PROCHIC TABLETS 0.6MG | 未提供 | 未提供 |
| HK-60287 | COLCHILY TAB 0.6MG | 未提供 | 未提供 |

（共 10 張有效單方許可證，此處列出 5 張。）

---

## 安全性考量

- **禁忌／需謹慎的疾病（來自知識圖譜，非仿單內容）**：肝衰竭、血液疾病、血小板減少、嗜中性白血球減少與顆粒球缺乏症、再生不良性貧血、消化性潰瘍、肌病變與橫紋肌溶解、腹瀉性疾病、腎功能不全、急性尿酸腎病變等。
- **藥物交互作用**：共查得 100 筆，以下為部分重大（Major）交互作用：
  - Clarithromycin、Cobicistat、Aprepitant、Rolapitant（可能影響 CYP3A4／P-醣蛋白代謝）
  - Rosuvastatin、Simvastatin（可能增加肌肉毒性風險）
  - Eliglustat、Deferiprone
- 中度（Moderate）交互作用包括 Metronidazole、Cimetidine、Chloroquine、Ticagrelor 等。其中 **Chloroquine** 是抗瘧疾藥物，若未來考慮用於瘧疾，需特別留意合併使用。

仿單的警語與禁忌資料尚未取得，詳細資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測，沒有任何臨床試驗，兩篇文獻也都是間接的前臨床研究（其中一篇研究的甚至不是 colchicine）。
- Colchicine 治療指數窄、對宿主細胞有毒性，且已有許多有效的抗瘧疾藥物，缺乏推進的理由。

**若要推進需要：**
- 體外實驗驗證 colchicine 對惡性瘧原蟲的活性，並評估與宿主細胞毒性之間的選擇性指數
- 作用機轉資料與仿單安全性資料（警語、禁忌）
- 動物模型的療效與安全性數據
- 評估與現有抗瘧疾藥物（如氯喹）合併使用的交互作用

---

### 補充：其他預測適應症

- **家族性地中海熱（體染色體顯性型）**：分數 99.38%，證據等級 L4，已有 19 篇文獻，多為綜述。Colchicine 本來就是家族性地中海熱的標準第一線治療，這項預測更像是原適應症的亞型延伸，而非真正的藥物再利用。文獻中沒有針對此亞型的 RCT 或登記試驗，建議列為研究問題。
- **隆突性皮膚纖維肉瘤**：分數 99.37%，證據等級 L5，無任何試驗或文獻。該病以手術和 imatinib 治療，colchicine 沒有明顯優勢，建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

