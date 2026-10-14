---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 780
evidence_level: L5
indication_count: 3
---

# Ritonavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Ritonavir：從 HIV 感染到猿猴免疫缺陷病毒感染

## 一句話總結

Ritonavir 是 HIV-1 蛋白酶抑制劑，也常作為藥物動力學增強劑，原本用於 HIV/AIDS 與 C 型肝炎感染的治療。
TxGNN 模型預測它可能對**猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)** 有效，
目前**無臨床試驗**，僅有 **10 篇文獻**（多為動物或體外研究）提供間接支持。

> 說明：模型排名第 1 的預測為「貓免疫缺陷症候群」，但該項無任何試驗與文獻，且屬獸醫適應症。本報告以有文獻佐證的排名第 2 項為主軸，並在文末簡述其他預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 C 型肝炎病毒感染、HIV 感染、AIDS（香港許可證未載明核准適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L4（僅有前臨床與體外研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ritonavir 是 HIV-1 蛋白酶抑制劑，同時為 CYP3A4 抑制劑，常用於增強其他抗病毒藥物的血中濃度（例如與 lopinavir、nirmatrelvir 組成複方）。其在 HIV 的療效已被證實，機轉上可能適用於近緣的慢病毒感染。

SIV 與 HIV 同屬慢病毒，是 HIV 研究中標準的非人類靈長類動物模型。體外研究顯示，SIVmac239 對 ritonavir 敏感（EC50 約 13 nM，HIV-1 約 25 nM，PMID 12709355），支持蛋白酶抑制機轉在 SIV 上同樣成立。

不過，TxGNN 的高分很可能反映的是與已知適應症（HIV/AIDS）在知識圖譜上的鄰近性，而非獨立證據。而且 SIV 感染是 HIV 的動物模型，對人類而言並非真正「新」的適應症，臨床再利用價值有限。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下表列出較相關的文獻（皆為前臨床或基礎研究，無 RCT）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | 體外感受性研究 | Antimicrob Agents Chemother | SIVmac239 對 ritonavir、indinavir、saquinavir 敏感，ritonavir EC50 約 13 nM |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | 體外感受性研究 | Antiviral Therapy | 評估 16 種已核准藥物對 HIV-2、SIV、SHIV 的活性，供治療與暴露後預防參考 |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | 動物研究 | J Virol Methods | 以 AZT、3TC 與 lopinavir/ritonavir 口服治療 SHIV 感染獼猴，觀察 CD8 亞群變化 |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | 動物研究 | J Virol | SIV 感染獼猴接受四藥抗病毒治療後病毒快速下降 |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | 動物研究 | PLoS Pathog | 強化多藥 ART 在猿猴 AIDS 模型中達成長期病毒抑制並限制病毒庫 |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | 動物研究 | PLoS One | 在 SIV 感染獼猴合併 cART 與 HDAC 抑制劑 SAHA，探討病毒庫 |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | 動物研究／回顧 | mBio | 慢病毒在腦部於有效 ART 下仍持續存在 |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | 動物研究 | Microbes Infect | 建構含 HIV-1 蛋白酶基因的 SHIV，作為蛋白酶抑制劑體內療效測試工具 |

**備註：** 另有 PMID 11364629、9875393、12186895 與 ritonavir 在 SIV 的療效僅有鬆散關聯，未列入。上述多篇動物研究是否使用 ritonavir，無法由現有摘要確認。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68558 | RITONAVIR TABLETS USP 100MG（Viatris） | 錠劑 | 未載明 |
| HK-61528 | NORVIR TABLET 100MG（AbbVie） | 錠劑 | 未載明 |
| HK-68129 | LOPINAVIR AND RITONAVIR TABLETS USP 200MG/50MG（Chemill） | 錠劑 | 未載明 |
| HK-65831 | LOPINAVIR AND RITONAVIR TABLETS USP 200MG/50MG（Viatris） | 錠劑 | 未載明 |
| HK-67683 | PAXLOVID TABLETS（Pfizer） | 錠劑 | 未載明 |

香港共有 10 張有效單一成分許可證，無已註銷者。

---

## 安全性考量

- **知識圖譜標示的相關風險族群（非仿單文字）：** 長 QT 症候群、尖端扭轉型心室頻脈、心臟傳導疾病、房室傳導阻滯、心肌病變、冠心病、胰臟炎、肝病與肝硬化、高血糖／糖尿病、糖尿病酮酸中毒、高三酸甘油脂血症、高尿酸血症／痛風、高膽紅素血症（含 Gilbert 症候群）、慢性 B 型肝炎、血友病等。
- **藥物交互作用：** 共記錄 100 筆。列出的項目中，屬 **Major** 的包括 loperamide、triamcinolone、budesonide；屬 Moderate 的包括 clarithromycin、metformin、dexamethasone、hydrocortisone、bupropion、aprepitant、metronidazole 等。Ritonavir 為強效 CYP3A4 抑制劑，用藥前需完整審視併用藥物。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測目標 SIV 感染是 HIV 的動物模型，對人類而言並非新的臨床適應症，且無任何臨床試驗；現有證據僅為間接的前臨床與體外研究，TxGNN 高分很可能只反映與 HIV 的圖譜鄰近性。
- Ritonavir 在香港雖已廣泛上市，但交互作用多（100 筆）且有多項心臟、肝臟、代謝相關風險，沒有明確新增臨床價值時不宜推進。

**若要推進需要：**
- 確認動物研究中是否實際使用 ritonavir，並取得 ritonavir 單藥或增強劑角色的療效資料
- 明確的作用機轉資料（MOA）
- 釐清此預測的目標用途（人類臨床、獸醫或研究模型）
- 取得香港仿單的警語與禁忌資料，完成安全性評估

---

## 其他預測適應症（簡述）

- **貓免疫缺陷症候群（排名 1，99.92%）：** 無試驗與文獻，屬獸醫適應症，FIV 蛋白酶對抑制劑的敏感性與 HIV 不同，療效未經驗證。證據等級 L5，決策 Hold。
- **伴共濟失調步態、無語言與皮質白質減少的神經發展障礙（排名 3，99.92%）：** 未找到合理的機轉關聯，無試驗與文獻，且 ritonavir 中樞神經穿透有限。證據等級 L5，決策 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

