---
layout: default
title: Colchicine
parent: 中證據等級 (L3-L4)
nav_order: 222
evidence_level: L4
indication_count: 3
---

# Colchicine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Colchicine：從痛風等既有用途到惡性瘧原蟲瘧疾

## 一句話總結

Colchicine（秋水仙素）在香港已上市，文獻顯示它主要用於痛風與家族性地中海熱。
TxGNN 模型預測它可能對**惡性瘧原蟲瘧疾 (Plasmodium falciparum malaria)** 有效，但目前**沒有臨床試驗**，只有 **6 篇**前臨床或血清學文獻，證據偏弱，建議先暫緩。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明；文獻指出主要用於痛風與家族性地中海熱 |
| 預測新適應症 | 惡性瘧原蟲瘧疾 (Plasmodium falciparum malaria) |
| TxGNN 預測分數 | 99.60% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Colchicine 是微管聚合抑制劑，會干擾細胞骨架的微管結構。

多項體外研究發現，結合瘧原蟲細胞骨架蛋白（如微管蛋白）的化合物，能抑制惡性瘧原蟲生長。其中一篇研究還指出，瘧原蟲的微管蛋白與哺乳類在分子層面差異很大。因此從標靶類別來看，這個預測在生物學上說得通。

不過，這六篇文獻都是前臨床或血清學研究，沒有任何一篇直接測試 Colchicine 用於瘧疾。此外，Colchicine 的治療指數很窄，在缺乏臨床資料的情況下不宜推進。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | 體外研究 | PloS one | 薑黃素會破壞惡性瘧原蟲的微管，顯示微管是可行的標靶 |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | 體外研究 | Molecular and cellular biology | 瘧原蟲 pfmdr1 基因在哺乳類細胞中表現後，細胞對氯喹更敏感 |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | 體外研究 | Antimicrob Agents Chemother | 探討 tubulozole 抗瘧的作用方式；Colcemid 對蛋白質合成的影響與其相似 |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | 體外研究 | Cell Biol Int Rep | 多種結合細胞骨架蛋白的化合物在體外對惡性瘧原蟲有活性 |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | 體外研究 | Cell Biol Int Rep | 與上一篇同一研究（重複收錄）；瘧原蟲微管蛋白與哺乳類差異明顯 |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | 觀察性（血清學） | Clin Exp Immunol | 急性瘧疾患者血清中，82% 有抗中間絲抗體 |

## 香港上市資訊

香港共有 10 張許可證，以下列出 5 張主要許可證。資料中未載明劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-37807 | COLGOUT TAB 0.5MG | Aspen Pharmacare Asia Limited |
| HK-60077 | COLCHICINE TAB 0.5MG | Welldone Pharmaceuticals Limited |
| HK-44403 | COLCHICINE TAB 500MCG (SYNCO) | Synco (H.K.) Limited |
| HK-66396 | PROCHIC TABLETS 0.6MG | Deltapharm Limited |
| HK-60287 | COLCHILY TAB 0.6MG | Star Medical Supplies Ltd |

## 安全性考量

- **治療指數窄**：文獻指出 Colchicine 的無毒、中毒與致死劑量之間沒有明確界線，非蓄意的中毒很常見，且常與不良預後相關（PMID 20586571）。

完整的警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有體外與血清學研究，沒有任何 Colchicine 用於瘧疾的臨床資料，證據等級僅 L4。
- Colchicine 的治療指數窄，缺乏臨床證據時不宜推進。

**若要推進需要：**
- 直接測試 Colchicine 抗惡性瘧原蟲的體外或動物實驗
- 取得香港衛生署仿單的警語與禁忌症
- 取得完整的作用機轉資料

**其他預測適應症備註：**
- **家族性地中海熱**（TxGNN 分數 99.38%）：證據等級 L3，建議 Proceed with Guardrails。文獻以 FMF 綜述為主，Colchicine 也是文獻公認的標準治療，因此這較可能是既有適應症，不是新用途，需對照仿單確認。推進時的防護重點是腎肝功能不全時調整劑量、篩檢 CYP3A4/P-gp 交互作用，以及注意中毒風險。
- **隆突性皮膚纖維肉瘤**（TxGNN 分數 99.37%）：證據等級 L5，僅有模型預測，建議 Hold。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

